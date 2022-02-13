from datetime import timedelta, timezone,datetime  
import csv
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

base_path=os.getcwd() #파일 경로

#id 정보 가져오고 날짜 파일에 저장
def input_data(user_id,path,today):
  user=[]
  
  #해당 id의 정보 가져온 후 시간 정보와 함께 리스트에 저장
  f = open('ID.csv','r',encoding='utf-8') 
  rdr=csv.reader(f)
  
  for dt in rdr:
    if user_id==dt[0]:
      user=dt  #data를 user에 대입 
      user[0]=datetime.now(timezone(timedelta(hours=9))).strftime('%H:%M:%S') 
      #id 부분은 삭제하고 시간 정보 넣음 
      break
    
  f.close()
  
  pygame.mixer.init()
  
  if len(user)==0:
    mySound2 = pygame.mixer.Sound( "sound/wrong.wav" )
    mySound2.play()
    return print('잘못된 qrcode 이거나 해당 ID가 존재하지 않습니다.')
    
    
  else:
    
    mySound = pygame.mixer.Sound( "sound/sound.wav" )
    mySound.play()
    
    
    os.chdir(path+"/entrylist/") #날짜 파일 저장 경로로 변경
    
    f=open(today+'.csv','a',newline='')
    wr = csv.writer(f)
    wr.writerow(user)
    f.close()
    
    os.chdir(path) #다시 기존 경로로 변경
    
    print("{}님 입장".format(user[1]))
    
    
    

#날짜 파일 생성 함수 
#새로운 파일에 정보 항목 작성 
def respone_date_csv(today):
  f=open('entrylist/'+today+'.csv','w',newline='') #entrylist 폴더에 날짜 파일 생성 
  wr = csv.writer(f)
  wr.writerow(['입장시간','아동 이름','아동 연락처','보호자 연락처','보호자와의 관계'])
  f.close()


#해당 명부 csv 파일이 존재하는지 확인
def jud_respone_csv(path,today):
  #jud = 파일 존재 여부 확인 변수 
  jud=os.path.exists(path+'/entrylist/'+today+'.csv') #존재하면 true 반환 
  if jud==False: respone_date_csv(today) #없을 시 생성 
  
  
#Ctrl+c 를 통한 프로그램 종료 
try:
  while True:
    today=str(datetime.now(timezone(timedelta(hours=9))).strftime('%Y-%m-%d'))
    jud_respone_csv(base_path,today)
    user_id=input('ID입력 : ')
    
    input_data(user_id,base_path,today)
except KeyboardInterrupt:
  print('QRcode 인식기 정지')