package tests;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class InfoKakera2 {

	public static void main(String[] args) {
		
//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**
		String[] fileNames = {//all file locations and names here in this format
"src/resources/flood-1.txt",
"src/resources/flood-2.txt",
"src/resources/flood-3.txt",
"src/resources/flood-4.txt",
"src/resources/flood-5.txt",
"src/resources/flood-6.txt",
"src/resources/flood-7.txt",
"src/resources/flood-8.txt",
"src/resources/flood-9.txt",
"src/resources/flood-husbando.txt",
"src/resources/flood-waifu.txt",
"src/resources/marry-roulette.txt"
};
//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**//**
		
		int[] totalOccurrences = {0, 0, 0, 0, 0, 0, 0, 0, 0};
							  //  P  :  T  G  Y  O  R  W  L
		
		for(String s : fileNames) {
			int[] occurrences = {0, 0, 0, 0, 0, 0, 0, 0, 0};
			//  P  :  T  G  Y  O  R  W  L
			String lastLine = "";
			try(BufferedReader reader = new BufferedReader(new FileReader(s))) {
				String line = reader.readLine();
				while(line != null) {
					int[] lineResults = {0, 0, 0, 0, 0, 0, 0, 0, 0};
									 //  P  :  T  G  Y  O  R  W  L
					if(line.contains("kakera") && lastLine.equals("{Reactions}")) { //if the line contains the desired message
						lineResults = getOccurrences(line.substring(0, 7)); //trims out the irrelevant info
					}
					
					for(int i=0;i<lineResults.length;i++) {
						occurrences[i] += lineResults[i];
					}
					
					lastLine = line; //remember the last line
					line = reader.readLine(); //read and go to the next line
				}
				
				//print results
				
//				System.out.println("Purple: "+occurrences[0]);
//				System.out.println("Normal: "+occurrences[1]);
//				System.out.println("Teal: "+occurrences[2]);
//				System.out.println("Green: "+occurrences[3]);
//				System.out.println("Yellow: "+occurrences[4]);
//				System.out.println("Orange: "+occurrences[5]);
//				System.out.println("Red: "+occurrences[6]);
//				System.out.println("Rainbow: "+occurrences[7]);
//				System.out.println("Light: "+occurrences[8]);
//				System.out.println();
				 
				
			} catch(IOException e) {
				e.printStackTrace();
			}
			
			for(int i=0;i<9;i++) { //add results from file to total results
				totalOccurrences[i] += occurrences[i];
			}
		}
		
		//print total results
		System.out.println();
		System.out.println("Total results:");
		System.out.println("Purple: "+totalOccurrences[0]);
		System.out.println("Blue: "+totalOccurrences[1]);
		System.out.println("Teal: "+totalOccurrences[2]);
		System.out.println("Green: "+totalOccurrences[3]);
		System.out.println("Yellow: "+totalOccurrences[4]);
		System.out.println("Orange: "+totalOccurrences[5]);
		System.out.println("Red: "+totalOccurrences[6]);
		System.out.println("Rainbow: "+totalOccurrences[7]);
		System.out.println("Light: "+totalOccurrences[8]);
		
	}
	
	public static int[] getOccurrences(String line) {
		int[] occurrences = {0, 0, 0, 0, 0, 0, 0, 0, 0};
						 //  P     T  G  Y  O  R  W  L
		
		switch(line.charAt(6)) {
		case 'P':
			occurrences[0] += 1;
			break;
		case ' ':
			occurrences[1] += 1;
			break;
		case 'T':
			occurrences[2] += 1;
			break;
		case 'G':
			occurrences[3] += 1;
			break;
		case 'Y':
			occurrences[4] += 1;
			break;
		case 'O':
			occurrences[5] += 1;
			break;
		case 'R':
			occurrences[6] += 1;
			break;
		case 'W':
			occurrences[7] += 1;
			break;
		case 'L':
			occurrences[8] += 1;
			break;
		default:
			System.out.println(line);
		}
		
		return occurrences;
	}

}
