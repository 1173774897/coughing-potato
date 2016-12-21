package dao;

import java.util.List;

import entity.Book;

public interface BookDao {
	public static String id = "";
	public static String isbn = "";
	public static String category = "";

	/**
	 * 
	 * @param id
	 * @return 
	 */
    public Book getBookInfoById(String id);
    
    /**
     * 
     * @param isbn
     * @return
     */
    public Book getBookInfoByIsbn(String isbn);

    /**
     * 
     * @param category
     * @return
     */
    public List<String> getBookIdsByCategory(String category);
}
