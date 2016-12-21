package dao.Impl;

import java.util.Iterator;
import java.util.List;

import entity.Book;

public class test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Book book = new Book();
        String isbn = "9787530201244";
        bookDaoImpl bdi = new bookDaoImpl();
        book = bdi.getBookInfoByIsbn(isbn);
        
        String author = book.getAuthor();
        String title = book.getTitle();
        String pic = book.getPic();
        String description = book.getDescription();
        Double doubanrating = book.getDoubanrating();
        
        System.out.println(author);
        System.out.println(title);
        System.out.println(pic);
        System.out.println(description);
        System.out.println(doubanrating);
        
        String category = "生活-游记";
        List<String> ids = bdi.getBookIdsByCategory(category);
        int len = ids.size();
        System.out.println(len);
        
        Iterator<String> it = ids.iterator();
        while(it.hasNext()){
        	String id = it.next();
        	System.out.print(id+" ");
        }
        
    	System.out.println('\n');

        for(String id : ids){
        	System.out.print(id+" ");
        }
        
	}

}
