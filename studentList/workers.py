# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
from textblob import TextBlob
from statistics import mean
from json import loads, dumps
from profDetailed.models import profDetailed
from studentDetailed.models import studentDetailed



def getList(pk):
	prof = profDetailed.objects.get(pk=pk)
	stuList = studentDetailed.objects.filter(cgpa__gte=prof.minCgpa, yearOfStudy__gte=prof.minYearOfStudy)

	# The generic weightage order is : WorkEx > skillsInterest > personalProjects > publications > branch > cgpa > yearOfStudy
	w = [0.250, 0.214, 0.178, 0.143, 0.107, 0.072, 0.036]

	s = list()

	for student in stuList:

		# Convert all the TextField string into objects to manipulate
		workExObj = loads(student.workEx)
		skillsInterestObj = loads(student.skillsInterest)
		personalProjectsObj = loads(student.personalProjects)
		publicationsObj = loads(student.publications)

		s0 = w[0]*processWorkExObj(workExObj, prof.areas, prof.keywords)
		s1 = w[1]*processSkillsInterestObj(skillsInterestObj, prof.areas, prof.keywords)
		s2 = w[2]*processPersonalProjectsObj(personalProjectsObj, prof.areas, prof.keywords)
		s3 = w[3]*processPublicationsObj(publicationsObj, prof.areas, prof.keywords)
		s4 = w[4]*processBranch(student.branch,prof.branch)
		s5 = w[5]*(student.cgpa - prof.minCgpa)
		s6 = w[6]*(student.yearOfStudy - prof.minCgpa)
		score = s0+s1+s2+s3+s4+s5+s6
		print(score)
		s.append([student.username, score])

	scores = sorted(s, key=lambda l: l[1], reverse=True)

	newList = list()
	for element in scores:
		newList.append({'username': element[0]})

	return newList


def processWorkExObj(workExObj, areas, keywords):

	values = list()

	for eachObj in workExObj:
		description = TextBlob(eachObj['description'])

		nouns = list()

		for tuple in description.tags:
			if (tuple[1] == 'NN') or (tuple[1] == 'NNS') or (tuple[1]=='NNP') :
				nouns.append(tuple[0])
		nouns = [noun.lower() for noun in nouns]

		keywords = loads(keywords)
		keywords = [keyword.lower() for keyword in keywords]

		areas = loads(areas)
		areas = [area.lower() for area in areas]

		unitedKeywords = list(set(keywords).union(areas))

		finalList = list(set(unitedKeywords).intersection(nouns))

		values.append(len(finalList)/len(unitedKeywords))

	return mean(values)*100

def processSkillsInterestObj(skillsInterestObj, areas, keywords):

	values = list()


	studentAreas = skillsInterestObj['areas']
	studentKeywords = skillsInterestObj['keywords']
	unitedStudentKeywords = list(set(studentAreas).union(studentKeywords))
	unitedStudentKeywords = [word.lower() for word in unitedStudentKeywords]

	keywords = loads(keywords)
	keywords = [keyword.lower() for keyword in keywords]

	areas = loads(areas)
	areas = [area.lower() for area in areas]

	unitedKeywords = list(set(keywords).union(areas))


	finalList = list(set(unitedKeywords).intersection(unitedStudentKeywords))

	values.append(len(finalList)/len(unitedKeywords))

	return mean(values)*100


def processPersonalProjectsObj(personalProjectsObj, areas, keywords):

	values = list()

	for eachObj in personalProjectsObj:
		description = TextBlob(eachObj['description'])

		nouns = list()

		for wordTuple in description.tags:
			if (wordTuple[1] == 'NN') or (wordTuple[1] == 'NNS') or (wordTuple[1] == 'NNP'):
				nouns.append(wordTuple[0])
		nouns = [noun.lower() for noun in nouns]


		keywords = loads(keywords)
		keywords = [keyword.lower() for keyword in keywords]

		areas = loads(areas)
		areas = [area.lower() for area in areas]

		unitedKeywords = list(set(keywords).union(areas))

		finalList = list(set(unitedKeywords).intersection(nouns))

		values.append(len(finalList)/len(unitedKeywords))

	return mean(values)*100

def processPublicationsObj(publicationsObj, areas, keywords):

	values = list()

	for eachObj in publicationsObj:
		description = TextBlob(eachObj['description'])

		nouns = list()

		for tuple in description.tags:
			if (tuple[1] == 'NN') or (tuple[1] == 'NNS') or (tuple[1]=='NNP') :
				nouns.append(tuple[0])
		nouns = [noun.lower() for noun in nouns]

		keywords = loads(keywords)
		keywords = [keyword.lower() for keyword in keywords]

		areas = loads(areas)
		areas = [area.lower() for area in areas]

		unitedKeywords = list(set(keywords).union(areas))

		finalList = list(set(unitedKeywords).intersection(nouns))

		values.append(len(finalList)/len(unitedKeywords))

	return mean(values)*100

def processBranch(branch,profBranch):

	profBranch = loads(profBranch)

	if branch in profBranch:
		return 100

	else:
		return 0







