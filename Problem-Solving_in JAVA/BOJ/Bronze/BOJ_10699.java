import java.io.*;
import java.time.*;
import java.time.format.DateTimeFormatter;
import java.util.*;


public class BOJ_10699 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ZonedDateTime nowSeoul = ZonedDateTime.now(ZoneId.of("Asia/Seoul"));
		DateTimeFormatter formatter = DateTimeFormatter.ofPattern("YYYY-MM-dd");
		System.out.println(nowSeoul.format(formatter));

	}

}
