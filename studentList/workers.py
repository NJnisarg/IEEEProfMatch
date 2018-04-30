from profDetailed.models import profDetailed
from studentDetailed.models import studentDetailed


class studentListWorker():
	def getList(pk):
		prof = profDetailed.objects.get(pk=pk)
		stuList = studentDetailed.objects.filter(cgpa__gte=prof.minCgpa,yearOfStudy__gte=prof.minYearOfStudy,workEx__gte=prof.minWorkEx)
		return stuList

	

