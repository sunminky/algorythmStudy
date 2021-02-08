import argparse

parser = argparse.ArgumentParser(description="parameter practice")

#고정 인자들(무조건 인자를 넣어줘야함)
parser.add_argument("parm1",type=int)   #parm1이라는 이름으로 파라메터 받음, 타입은 int(기본값은 None)
parser.add_argument("parm2",type=str)   ##parm2이라는 이름으로 파라메터 받음, 타입은 str

#고정인자 아님(넣어도 되고 안넣어도 되고)
parser.add_argument("dynparm",nargs='*')  #여러개의 인자를 받을수 있음, *(0개 이상), +(1개 이상), ?(0개나 1개)
parser.add_argument("-c",action="store",dest="comment",type=str,default="No Comment")   #str로 변환되서 comment라는 이름으로 저장(기본값 액션), 옵션 안주면 기본값인 No Comment로 설정
parser.add_argument("--true",action="store_true",dest="tVar")       #옵션을 주면 true가 저장됨
parser.add_argument("--false",action="store_false",dest="fVar")     #옵션을 주면 false가 저장됨
parser.add_argument("--big",action="store_const",const=10.0)        #옵션을 주면 10.0이 저장됨
parser.add_argument("-a",action="append",type=str)  #-a로 준 값들이 리스트로 모여서 반환됨
parser.add_argument("--version",action="version",version="%(prog)s 1.0")    #버전을 출력

args = parser.parse_args()              #명령줄에서 받은 인자들은 처리함
#print("파라메터1 : {}, 파라메터2 : {}".format(args.parm1,args.parm2))   #인자들은 parse_args()로 얻은 객체.파라메터이름 으로 호출가능
print(parser.parse_args())  #매개변수들 보기
print(args.comment)         #이름으로 매개변수에 접근하기