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


#Peter = Student(name="Peter", age=34, tracks=[Bob.tracks, "UI","UX"], score=20.90)

# Class Variable
Peter = 'student'

def change_name(self, new_name):
  self.name = new_name
  setattr(Bob, 'Name', Peter)
  
def change_age(self, new_age):
  self.age = new_age
  setattr(Bob, 'Age', 34)

class Student:
 def append_tracks(self, new_tracks):
  super('Tracks: ', Bob.tracks).append(new_tracks)
  self.track = new_tracks
  
def get_score(self, score):
  self.score = score
  getattr(Bob, 'score')

print('Student Two Details:')
print('Name: ', Peter.new_name)
print('Age: ', Peter.age)
print('Tracks: ', Peter.tracks)
print('Score: ', Peter.score)