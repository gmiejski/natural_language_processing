from impl.LevensteinDistance import LevensteinDistance

string1 = "kura"
string2 = "kurka"

levenstein_distance = LevensteinDistance()
print levenstein_distance.create_matrix(string2, string1)



