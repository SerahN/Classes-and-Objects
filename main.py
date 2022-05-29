class Student:

    # Class Variable
    Bob = 'student'

    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        

    # Instance Variable
     self.name = name
     self.age = age
     self.tracks = tracks
     self.score = score

Bob = Student(name="Bob", age=26, tracks=["FE","BE"], score=20.90)

print('Student One Details:')
print('Name: ', Bob.name)
print('Age: ', Bob.age)
print('Tracks: ', Bob.tracks)
print('Score: ', Bob.score)

class Student():
    name = "Bob"
    age = 26
    tracks = ['FE', 'BE']
    score = 20.9

    #print('Name:', hasattr(Bob, 'name'))
    #print('Age:', hasattr(Bob, 'age'))
    #print('Tracks:', hasattr(Bob, 'tracks'))
    #print('Score:', hasattr(Bob, 'score'))

    print('Student Two Details:')
    setattr(Bob, 'name', 'Peter')
    print('Name:', Bob.name)
    setattr(Bob, 'age', 34)
    print('Age:', Bob.age)
    getattr(Bob, 'score')
    print('Score:', Bob.score)

    class Student():
     def __init__(self):
      self.tracks = ['FE', 'BE']
      new_tracks = ['UI', 'UX']
      self.tracks.append(new_tracks)
    print('Tracks: ', Bob.tracks.append[tracks])

