using System;
public static class HelloWorld
{
    public static string Hello() => "Hello, World!";

    public static void Main()
    {
        string message = Hello();
        Console.WriteLine(message);
    }
}
