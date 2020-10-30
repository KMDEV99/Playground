/*
Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
*/
public class Kata {

  public static String high(String str) {
    // Your code here...
        str = str.toLowerCase();
        String[] arr = str.split(" ");
        int tab[] = new int[arr.length];
        int i = 0;
        int max = 0;
        int score;
        int searchIndex = 0;

        for (String word : arr) {
            for (char ch : word.toCharArray()) {
                score = Character.getNumericValue(ch) - 9;
                tab[i] += score;
            }
            if (tab[i] > max)
                max = tab[i];
            i += 1;
        }
        for (int index=0;index<tab.length;index++)
            if (tab[index]==max)
                searchIndex = index;

        return arr[searchIndex];
  }

}