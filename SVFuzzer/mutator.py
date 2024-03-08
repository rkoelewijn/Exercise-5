import random
import string

class Mutator:
    def mutate(self, s: str):
        """
        randomly stack mutators 1-5 times.

        :param s: the input string
        :return s: the mutated string
        """
        # Select the amount of mutations we are going to do
        n = random.randint(1,5) 
        
        # Apply the mutations
        for m in range(0,n):
            # We choose the random mutation
            mutation = random.randint(0,4)
            if mutation == 0: 
                s = self.insert_random_character(s)
            elif mutation == 1: 
                s = self.invert_characters(s)
            elif mutation == 2: 
                s = self.remove_random_character(s)
            elif mutation == 3: 
                s = self.scramble_characters(s)
            elif mutation == 4: 
                s = self.swap_characters(s) 
        return s

    @staticmethod
    def insert_random_character(s: str) -> str:
        """
        insert a character from ASCII printable characters and the extended ASCII codes at a random position

        :param s: the input string
        :return s: the mutated string
        """
        
        # Choose a random position
        random_pos = random.randint(0,len(s))
        #Choose a random char out of the sets of letters, digits and punnctuatution marks(all ascII chars)
        random_char = random.choice(string.ascii_letters + string.digits + string.punctuation)
        # Prints s until the random position adds the random_char and prints the rest 
        s =s[:random_pos] + random_char + s[random_pos:]
        
        return s

    @staticmethod
    def remove_random_character(s: str) -> str:
        """
        remove a random character from the string

        :param s: the input string
        :return s: the mutated string
        """

        if len(s) > 0:

            # Choose a random position
            random_pos = random.randint(0,len(s)-1)
            # Prints s until the random pos skip the random position and print the next part of s.
            s = s[:random_pos] + s[(random_pos+1):]

        return s

    @staticmethod
    def swap_characters(s: str) -> str:
        """
        randomly swap two characters of the string

        :param s: the input string
        :return s: the mutated string
        """

        if len(s) > 0:
            # We select two random positions 
            pos1 = random.randint(0,len(s)-1)
            pos2 = random.randint(0, len(s)-1)

            # Because there is a possability that the two might have the same value, if that is the case we change pos2 untill this is no longer true. 
            while pos1 == pos2:
                pos2 = random.randint(0,len(s)-1)
            
            # Save the character in those positions 
            char1 = s[pos1]
            char2= s[pos2] 
            
            # Swap the two characters 
            s[pos1] = char2
            s[pos2] = char1 
                
        return s

    @staticmethod
    def scramble_characters(s: str) -> str:
        """
        select a random number of characters from the string (which may not be contiguous)
        and randomly shuffle their values

        :param s: the input string
        :return s: the mutated string
        """

        # Create the random number of characters we will select
        n = random.randint(0,len(s)-1)

        # Create arrays to keep track of our chars and their previous positions
        selected_char = [] 
        selected_pos = []  

        # We select the random chars (which may or not be contiguous) and their positions where they came from
        for i in range(0,n):
            pos = random.randint(0,len(s)-1)

            # If we have already picked this position, we swap for a different one. 
            while pos in selected_pos:
                pos = random.randint(0, len(s)-1)

            # Save the position and the char
            selected_pos.append(pos)
            selected_char.append(s[pos])
        
        # Shuffle the chars 
        random.shuffle(selected_char)
        # Put them into the string 
        for i in selected_pos:
            s[i] = selected_char[i]

        return s

    @staticmethod
    def invert_characters(s: str) -> str:
        """
        select a random number of contiguous characters from the string and reverse their order

        :param s: the input string
        :return s: the mutated string
        """
        # If length of s is smaller then 2 we can't reverse
        if len(s)>1:

            #Chooses a random position to start reversing
            random_pos = random.randint(0,len(s)-2)
            
            random_length = random.randint(1,len(s) - random_pos)
            
            substring = s[random_pos:random_pos+random_length]
            
            reversed_substring = substring[::-1]

            s= s[:random_pos] + reversed_substring + s[random_pos+random_length:]

            
        return s


