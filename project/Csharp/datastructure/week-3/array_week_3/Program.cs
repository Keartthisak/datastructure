using System;
using System.Diagnostics.Contracts;
using System.Runtime.CompilerServices;
using System.Xml.Schema;

class Program
{
    static void Main()
    {
        int[] scores = {10, 20, 30 ,40, 50, 60 ,70, 80 ,90}; //
        Console.WriteLine("รายการข้อมูลใน Array :");
        //for Loop
        for (int i =0; i < scores.Length; i++)
        {
            Console.WriteLine($"index {i} = {scores[i]}");
        
        }
        //foreach
        foreach(int x in scores)
        {
            Console.WriteLine($"Value is :{x}");
        } 
        //forsum
        int sum = 0;
        for (int i =0; i < scores.Length; i++)
        {
            sum += scores[i];
        }
        Console.WriteLine($"Sum ={sum}");  // ผลรวม
        double avg = (double)sum / scores.Length;
        Console.WriteLine($"Average : {avg}"); // ค่าเฉลี่ย
        //for max, min
        int max = scores[0];
        int min = scores[0];
        for (int i = 0; i < scores.Length; i++)
        {
            // Max value check
            if(scores[i] > max)
            {
                max = scores[i];
            }
            // min value check
            if(scores[i] < min)
            {
                min = scores[i];
            }
        }
         Console.WriteLine($"max ={max}"); 
         Console.WriteLine($"min ={min}");
        
    }

}
