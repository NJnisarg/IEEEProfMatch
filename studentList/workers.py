# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process
from textblob import TextBlob
from statistics import mean
from json import loads, dumps
from profDetailed.models import profDetailed
from studentDetailed.models import studentDetailed



def getList(pk):
	prof = profDetailed.objects.get(pk=pk)
	if prof is None:
		return list()

	if (prof.minCgpa is None) or (prof.minYearOfStudy is None) or (prof.areas is None) or (prof.keywords is None) or (prof.branch is None) or (prof.minWorkEx is None):
		return list()

	stuList = studentDetailed.objects.filter(cgpa__gte=prof.minCgpa, yearOfStudy__gte=prof.minYearOfStudy)

	if len(stuList) == 0:
		return list()

	# The generic weightage order is : WorkEx > skillsInterest > personalProjects > publications > branch > cgpa > yearOfStudy
	w = [0.250, 0.214, 0.178, 0.143, 0.107, 0.072, 0.036]

	s = list()

	for student in stuList:

		if (student.workEx is None) or (student.workEx is ""):
			workExObj = None
		else:
			workExObj = loads(student.workEx)

		if (student.skillsInterest is None) or (student.skillsInterest is ""):
			skillsInterestObj= None
		else:
			skillsInterestObj = loads(student.skillsInterest)

		if (student.personalProjects is None) or (student.personalProjects is ""):
			personalProjectsObj = None
		else:
			personalProjectsObj = loads(student.personalProjects)

		if (student.publications is None) or (student.publications is ""):
			publicationsObj = None
		else:
			publicationsObj = loads(student.publications)

		# Convert all the TextField string into objects to manipulate

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

	if workExObj is None:
		return 0

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

	if skillsInterestObj is None:
		return 0

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

	if personalProjectsObj is None:
		return 0

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

	if publicationsObj is None:
		return 0

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

	if branch is None:
		return 0

	profBranch = loads(profBranch)

	if branch in profBranch:
		return 100

	else:
		return 0







