import pickle

data = ("Data", 10, [x*x for x in range(5)])
data2 = ("Data2", 100, [x*x for x in range(5, 10)])
data3 = ("Data3", 1000, [x*x for x in range(10, 15)])
with open("test.pickle", "wb") as f:
    pickle.dump(data, f)   #객체를 파일로 출력
    pickle.dump(data2, f)  # 객체를 파일로 출력
    byte_data = pickle.dumps(data3)  #피클링 객체를 바이트로 출력
    pickle.dump(byte_data, f)

with open("test.pickle", "rb") as f:
    restore_data = pickle.load(f)
    print(restore_data)
    restore_data2 = pickle.load(f)
    print(restore_data2)
    restore_data3 = pickle.load(f)
    print(pickle.loads(restore_data3))  #바이트로 출력된 피클링 객체 복구
