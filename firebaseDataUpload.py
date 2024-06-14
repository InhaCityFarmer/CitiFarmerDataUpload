import firebase_admin
from datetime import datetime

from firebase_admin import credentials
from firebase_admin import firestore

# Firebase 인증 정보를 제공하는 서비스 계정 키 파일을 다운로드하고 경로를 설정합니다.
cred = credentials.Certificate('./mykey.json')
firebase_admin.initialize_app(cred)

# Firestore 데이터베이스를 가져옵니다.
db = firestore.client()
now = datetime.now()
formate_now = now.strftime("%Y-%m-%d")



def update_fs(filepath):
    db = firestore.client()
    doc_ref = db.collection('User').document('TvAqbRIHDRNqS8GvqmLzFQyLFb93').collection('crop').document('tomato')
    
    doc = doc_ref.get()
    data = doc.to_dict()
    T_arr = data.get('t',[])
    D_arr = data.get('d',[])
    H_arr = data.get('h',[])
    M_arr = data.get('m',[])

    
    with open(filepath,'r') as file:
        line = file.readline()
        print(line)
        words = line.split()
        M = words[1] + "*" + formate_now
        D = words[3]+ "*" + formate_now
        T = words[5]+ "*" + formate_now
        H = words[7]+ "*" + formate_now
            
        T_arr.append(T)
        D_arr.append(D)
        H_arr.append(H)
        M_arr.append(M)
                          
    doc_ref.set({
    'm' : M_arr,
    'd' : D_arr,
    'h' : H_arr,
    't' : T_arr
    })



update_fs('input.txt')

