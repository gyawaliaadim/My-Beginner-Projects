import java.util.ArrayList;
import java.util.Scanner;

// imports

// num= first pair, given by user
// sqNum closest square of a number
// sideNum= (square number*2*10+x)+x
// subValue= num-square number^2
// finalSqrt= square root of that number (final answer)



public class sq_cal{

    static ArrayList<String> Pair(String input){
        ArrayList<String> pairedArray = new ArrayList<>();
        for (int i = 0; i < input.length(); i += 2) { // iterate from the first character to the last by 2 so, 2 characters each time
            // Ensure there's a valid pair to print
            if (i + 1 < input.length()) { // chat gpt code
                pairedArray.add(input.substring(i, i + 2)); // add the first and the second i(i, i+1)th character from the string to the array
                }
            }
        return pairedArray;
        }


    static ArrayList<String> make_pairs(String input){

        ArrayList<String> pairedArray = new ArrayList<>();
        if (input.contains(".")){
            String intPart = input.split("\\.")[0]; // seperate integer part and fraction part
            String fracPart = input.substring(input.indexOf('.') + 1).trim();

            if (intPart.length() % 2 == 1) { // check if the length is odd or even
                intPart="0"+intPart;
                }
            if (fracPart.length() % 2 == 1) { // check if the length is odd or even
                fracPart=fracPart+"0";// to always make it even, like 123->1230 1234->1234 in fractional part only
                }
            pairedArray.addAll(Pair(intPart));// add integer, decimal and fraction part
            pairedArray.add(".");
            pairedArray.addAll(Pair(fracPart));
        }
        else{
        if (input.length() % 2 == 1) { // check if the length is odd or even
            input="0"+input;
            }
            pairedArray=Pair(input);
        }
        return pairedArray;
    }


    
    static long[] calculation(String numStr, long sideNum, int first) {
        long num=Long.parseLong(numStr);
        // long sideNum = Long.parseLong(sideNumStr);
        // long first = Long.parseLong(firstStr);
        if (first==1){// check if its first time
            long sqNum=0;
            while (sqNum*sqNum<=num){//find the closest square root of a number
                sqNum=sqNum+1;
            }
            sqNum-=1;
            sideNum=(sqNum+sqNum)*10;// calculate the side number for the first time
            long subValue=((num-sqNum*sqNum));// calculate the sub value for the first time
            long[] result = {sideNum,subValue,sqNum}; // Storing both values in an array
            return result;
        }
        else{// when its not the first time
            long sqNum=0;
            while (((sideNum+sqNum)*sqNum)<=num){// finding for ex if the side num for the first time was 4, then it would be
                // (40+x)*x<=num , num means the sub_value+ the next pair in order
                sqNum=sqNum+1;
            }
            sqNum-=1;// sqNum means the square number
            long subValue=(num-((sideNum+sqNum)*sqNum));// sub value is the num( subvalue+next pair in order) - (40+x)*x
            sideNum=((sideNum+sqNum)+sqNum)*10;
            long[] result = {sideNum,subValue,sqNum }; // Storing both values in an array
            return result;
        }

    }
    static float userInput(String msg){
        Scanner sc = new Scanner(System.in);
        while (true){
            try{
                System.out.print(msg);
                return Float.parseFloat(sc.nextLine());
            }
            catch(Exception e){
                System.out.println("Enter a valid input.");
            }
        }
    }
    public static void main(String[] args) {
        float inp=userInput("Enter a number: ");
        ArrayList<String> listOfNumbers = new ArrayList<>();
        listOfNumbers=make_pairs(String.valueOf(inp));
        // float decimalPoints=0;
        String part="int";
        long sideNum=0;
        long subValue=0;
        String finalResult = "";
        // long sqNum=0;
        String num="";
        for (int index = 0; index < listOfNumbers.size(); index++){
            String pair=listOfNumbers.get(index);
            if (index==0){
                num=pair;
            }
            else{
                num=String.valueOf(subValue)+pair;
            }
            if (((listOfNumbers).size()==index+1 && part.contains("int")) || pair.contains(".")){
                finalResult=finalResult+".";
                long decimalPoints=(long) userInput("Enter Number of decimal points: ");
                int numberOfPairsAfterDecimalPoint= listOfNumbers.size() - (index + 1);       
                for (int j=0; j<(decimalPoints-numberOfPairsAfterDecimalPoint);j++){
                    listOfNumbers.add("00");
                }
                part="frac";
                if(pair.contains(".")){
                    continue;
                }
            }
            long[] result = calculation(num,sideNum,index);
            sideNum=result[0];
            subValue=result[1];
            long sqNum=result[2];

            finalResult=finalResult+String.valueOf(sqNum);
        } 
        System.out.println("The square root of "+inp+" is "+finalResult); 
        while (true){
            Scanner sc = new Scanner(System.in);
            System.out.println("Do you want to continue(y/n): ");
            String ask=sc.next();
            switch(ask.toLowerCase()) {
                case "y":
                  main(args);
                //   break;
                case "n":
                    System.exit(0);
                  // code block
                //   break;
                default:
                    System.out.println("Enter a valid input.");
                  // code block
              }
        }


    }
}

