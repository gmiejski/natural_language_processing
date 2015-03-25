from impl.LevensteinDistance import LevensteinDistance
from impl.SimiliarWordFinder import SimiliarWordFinder

string1 = "kura"
string2 = "kurka"

levenstein_distance = LevensteinDistance()
print levenstein_distance.create_matrix(string2, string1)

similiarWordFinder = SimiliarWordFinder()
similiarWordFinder.find_similiar_word("dupa")
similiarWordFinder.find_similiar_word_by_all("dupa")



