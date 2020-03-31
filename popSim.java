
/**
 * Simulate the impact of coronavirus(covid-19) in the world.
 *
 * @author Ishan Vepa
 * @date 03/22 - 28/20
 */
import java.util.Scanner;
public class popSim
{
    public static void main(String args[])
    {
        System.out.println("This program will simulate the impact of coronavirus(covid-19) in the world.\n");
        boolean iterate = false;
        int finalPop = 0;
        while(iterate == false)
            {   
            System.out.println("How much time (in days) would you like to simulate following ?");
        
            Scanner in = new Scanner(System.in);
            
            int time = in.nextInt();
            double rate = -0.3078108304;//change
            double a = 103.7220217; //as of jan 22
            int k = 58016;
            double h = 0;            
            int timePrint = 0;
            
            if(time == 26)
            {
                finalPop = 58016;
                timePrint = time;
            }
            else if(time > 26)
            {
                rate *= -1;
                h = -45.002;
                timePrint = time;
                time -= 26;
                finalPop = (int)calcFinalPop(a, rate, time, k, h);
            }
            else if(time < 26)
            {
                timePrint = time;
                finalPop = (int)calcFinalPop(a, rate, time, k, h);
            }
            
            
            
            
            System.out.println("In " + timePrint + " days, the population with the covid-19 virus will be " + finalPop + " people.");                       
            System.out.println("\nWould you like to simulate again (y/n)?");
            String choice = in.next();
            
            if(choice.equalsIgnoreCase("y"))
            iterate = false;
            else if(choice.equalsIgnoreCase("n"))
            iterate = true;
            else
            {
                System.out.println("You did not enter an appropriate option.\nTry again.\n");
                choice = in.next();
            }
        }     
        System.out.println("The program has concluded.");
                
                
      }
   
        public static double calcFinalPop(double aConst, double rate, int time, int k, double h)
       {   
        double e = Math.E; //eulers constant
        
        //double popF = (k * aConst * Math.pow(e, (rate * time))) / 
        //              (k + aConst * (Math.pow(e, (rate * time) - 1)));
        
        double popF = k / (1 + aConst * Math.pow(e, rate * (time + h))); 
        
        
        return popF;
      }   
   
   

      
}