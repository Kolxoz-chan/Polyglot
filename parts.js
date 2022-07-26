class Noun
{
	is_animacy = false	// Одушевлённое
	is_nomen = false	// Собственное
	gender = 1			// Род
	number = false		// Число
	case = 1			// Падеж
	
	getData()
	{
		return {
			"type" : "Noun",
			"is_animacy" : this.is_animacy,
			"is_nomen" : this.is_nomen,
			"gender" : this.gender,
			"number" : this.number,
			"case" : this.case
		}
	}
}
		
class Verb
{
	gender = 1			// Род
	number = false		// Число
	time = 1			// Время
	
	getData()
	{
		return 
		{
			"type" : "Verb",
			"gender" : this.gender,
			"number" : this.number,
			"time" : this.time
		}
	}
}