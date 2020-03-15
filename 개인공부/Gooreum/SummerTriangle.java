/*https://level.goorm.io/exam/49087/%EC%97%AC%EB%A6%84%EC%9D%98-%EB%8C%80%EC%82%BC%EA%B0%81%ED%98%95/quiz/1*/
/*수학공식들
* https://freshrimpsushi.tistory.com/482        //코사인의 덧셈 법칙
* https://blog.naver.com/dalsapcho/20131270309  //삼각형의 너비 구하는 공식
* https://ko.wikipedia.org/wiki/%EC%BD%94%EC%82%AC%EC%9D%B8_%EB%B2%95%EC%B9%99  //제 2코싸인 법칙
* */
package goorm;

import java.util.Scanner;

public class SummerTriangle {
    public static void main(String[] args) throws Exception {
        Scanner scanner = new Scanner(System.in);
        Location[] location = new Location[3];  //삼각형의 좌표 저장
        double sin = 0; //1번째 변과 2번째 변의 sin값 저장
        double cos = 0; //1번째 변과 2번째 변의 cos값 저장
        double area = 0;    //삼각형의 넓이 저장

        for(int i=0;i<location.length;i++){
            location[i] = new Location(scanner.nextInt(),scanner.nextInt());
        }

        for(int i=0;i<location.length;i++){ //0~1거리, 1~2거리, 2~0거리 저장함
            location[i].setDistance(calcDistance(location[i],location[(i+1)%3]));
        }
        cos= lawOfCosines(location[0],location[1],location[2]); //코사인 값 구함, 제2 코사인 법칙 사용
        sin = Math.sqrt(1 - cos*cos);   //코싸인의 덧셈 공식 사용
        area = 0.5 * sin * location[0].getDistance() * location[1].getDistance();   //넓이를 구함

        System.out.println(String.format("%.2f",area));     //소수 2번째 자리까지 반올림해서 출력

    }
    public static double calcDistance(Location a,Location b){   //거리구하는 함수, 2차원 평면에서 거리 구하는 공식 사용
        return Math.sqrt( (a.getX()-b.getX())*(a.getX()-b.getX()) + (a.getY()-b.getY())*(a.getY()-b.getY()) );
    }
    public static double lawOfCosines(Location a,Location b,Location c){    //제2 코사인 법칙
        return (a.getDistance()*a.getDistance() + b.getDistance()*b.getDistance() - c.getDistance()*c.getDistance()) / (2 * a.getDistance() * b.getDistance());
    }
    static class Location{
        private int x,y;    //x좌표, y좌표
        private double distance;    //현재 점부터 다음 점까지의 거리
        public Location(int x,int y){
            this.x = x;
            this.y = y;
        }

        public int getX() {
            return x;
        }

        public void setX(int x) {
            this.x = x;
        }

        public int getY() {
            return y;
        }

        public void setY(int y) {
            this.y = y;
        }

        public double getDistance() {
            return distance;
        }

        public void setDistance(double distance) {
            this.distance = distance;
        }
    }
}
