from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from profDetailed.models import profDetailed
from studentDetailed.models import studentDetailed


class studentListWorker():
	def getList(pk):
		prof = profDetailed.objects.get(pk=pk)
		stuList = studentDetailed.objects.filter(cgpa__gte=prof.minCgpa,yearOfStudy__gte=prof.minYearOfStudy,workEx__gte=prof.minWorkEx)

		## The generic weightage order is : WorkEx > keywords > areas > branch > cgpa > yearOfStudy
		w = [0.3,0.25,0.17,0.13,0.09,0.06]
		s = []
		for student in stuList:
			s0 = w[0]*(student.workEx - prof.minWorkEx);
			s1 = w[1]*fuzz.partial_ratio(student.skillsInterest,prof.keywords)
			s2 = w[2]*fuzz.partial_ratio(student.areas,prof.areas)
			s3 = w[3]*fuzz.partial_ratio(student.branch,prof.branch)
			s4 = w[4]*(student.cgpa - prof.minCgpa)
			s5 = w[5]*(student.yearOfStudy - prof.minYearOfStudy)
			score = s0+s1+s2+s3+s4+s5
			s.append([student.username,score])

		s = sorted(s,key=lambda l:l[1], reverse=True)

		newList=[]
		for element in s:
			newList.append({'username':element[0]})
		return newList




