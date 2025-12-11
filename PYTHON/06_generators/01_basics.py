def get_chai_gen():
    yield "cup1"
    yield "cup2"
    yield "cup3"

chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))
