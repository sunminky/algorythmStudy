package pregrammers;

public class Miller_RabinPrimalityTest {
    public static void main(String[] args) {
        new Miller_RabinPrimalityTest().primalityTest(221);
    }
    public boolean primalityTest(int n){
        int num = n-1;
        int d = 0;
        int s = 0;
        int[] a = {2, 7, 61};

        if(n % 2 == 0)  //n이 짝수이면 소수가 될수없으니까 종료
            return false;

        while(num%2 == 0){
            num = num / 2;
            s++;
        }
        d = num;

        for(int i=0;i<a.length;i++){
            if(!condition1(d,n,a[i]))
                return false;
            if(!condition2(d,n,s,a[i]))
                return false;
        }

        return false;
    }
    public boolean condition1(int d,int n,int a){   //a**d % n != 1
        if(repeatedSquaring(a,d,n) == 1)
            return false;
        return true;
    }
    public boolean condition2(int d,int n,int s,int a){   //a**(d* 2**0~s-1) == -1이 1개이상
        for(int i=0;i<s;i++){
            //미구현어엉어어
        }
        return false;
    }
    public int repeatedSquaring(int n,int sn,int division){ //너무 큰 제곱수의 나머지를 구해주는 함수
        String binSn = Integer.toBinaryString(sn);
        int result = 1;

        for(int i=0;i<binSn.length();i++){
            if(binSn.charAt(i) == '1'){
                result = result*result*n % division;
            }
            else{
                result = result*result % division;
            }
        }
        return result;
    }
}
