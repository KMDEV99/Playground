/*
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)
*/

public class HumanReadableTime {
  public static String makeReadable(int value) {
    String res = String.format("%s:%s:%s",  parseDate(value / 3600), parseDate(value / 60 % 60), parseDate(value % 60));
    return res;
  }
  public static String parseDate(int date)
    {
        String dateString = Integer.toString(date);
        return date > 9 ? dateString : "0" + dateString;
    }
}