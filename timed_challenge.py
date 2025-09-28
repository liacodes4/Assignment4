# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

#7. First Repeated Value
#Return the first value that repeats in the collection.
#Input: [1, 4, 3, 5, 3, 2, 1]
#Output: 3

def first_repeated_value(values):
    seen = set()
    for v in values:
        if v in seen:
            return v
        seen.add(v)
    return None

#Tests:
if __name__== "__main__":
    print(first_repeated_value([1,4,3,5,3,2,1]))
    print(first_repeated_value([2,1,6,7,67,67]))

#For this timed challenge, I picked the “First Repeated Value” problem.
#I chose to use a set because it’s simple and really good for checking if something has been seen before.
#With a set, adding and checking values only takes constant time, so I can go through the list once and stop as soon as I find a repeat. 
#It was the most straightforward way to solve the problem quickly and correctly.  
#The 30-minute time limit definitely shaped how I approached this. 
#Instead of overthinking different solutions, I went with the one I knew would work and that I could write confidently without getting stuck. 
#If I had more time, I might have experimented with other approaches, like keeping track of indexes or trying to return all duplicates instead of just the first one. 
#But with the clock ticking, I focused on getting a clear, working solution rather than exploring every option.  
#One compromise I made was not adding a lot of extra features or edge case handling. 
#For example, I didn’t build in logic for cases like empty input or multiple repeats beyond the first one, because that wasn’t necessary to solve the core problem. 
#I also didn’t spend much time writing out detailed test cases, other than a couple of quick checks. 
#Overall, the time pressure pushed me to stay focused and keep my solution as simple and direct as possible.  
