package dao.Impl;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.List;

import dao.BaseDao;
import dao.BookDao;
import entity.Book;

public class bookDaoImpl extends BaseDao implements BookDao{
    Connection conn = null;
    PreparedStatement stm = null;
    ResultSet rs = null;
	
	
	@Override
	public Book getBookInfoById(String id) {
		conn = BaseDao.getConnection();
		Book book = new Book();
		
		String sql = "SELECT * FROM booklist WHERE id = ?";
		try{
			stm = conn.prepareStatement(sql);
			stm.setString(1, id);
			
			rs = stm.executeQuery();
			
			if(rs.next()){
				book.setId(rs.getString("id"));
				book.setTitle(rs.getString("title"));
				book.setAuthor(rs.getString("author"));
				book.setTranslater(rs.getString("translator"));
				book.setPublisher(rs.getString("publisher"));
				book.setIsbn(rs.getString("isbn"));
				book.setPic(rs.getString("pic"));
				book.setDescription(rs.getString("description"));
				book.setDoubanrating(rs.getDouble("doubanrating"));
				book.setCategory(rs.getString("category"));
				book.setUpdateat(rs.getString("updateat"));
			}
		}catch(SQLException e){
			e.printStackTrace();
			return null;
		}finally{
			this.closeConnection(conn, stm, rs);
		}
		
		// TODO Auto-generated method stub
		return book;
	}

	@Override
	public Book getBookInfoByIsbn(String isbn) {
	    conn = BaseDao.getConnection();
		Book book = new Book();
		
		String sql = "SELECT * FROM booklist WHERE isbn = ?";
		try{
			stm = conn.prepareStatement(sql);
			stm.setString(1, isbn);
			
			rs = stm.executeQuery();
			
			if(rs.next()){
				book.setId(rs.getString("id"));
				book.setTitle(rs.getString("title"));
				book.setAuthor(rs.getString("author"));
				book.setTranslater(rs.getString("translator"));
				book.setPublisher(rs.getString("publisher"));
				book.setIsbn(rs.getString("isbn"));
				book.setPic(rs.getString("pic"));
				book.setDescription(rs.getString("description"));
				book.setDoubanrating(rs.getDouble("doubanrating"));
				book.setCategory(rs.getString("category"));
				book.setUpdateat(rs.getString("updateat"));
			}
		}catch(SQLException e){
			e.printStackTrace();
			return null;
		}finally{
			this.closeConnection(conn, stm, rs);
		}
		
		// TODO Auto-generated method stub
		return book;
	}

	@Override
	public List<String> getBookIdsByCategory(String category) {
		conn = BaseDao.getConnection();
		List<String> bookIdList = new ArrayList<String>();
		
		String sql = "SELECT id FROM booklist WHERE category = ?";
		try {
			stm = conn.prepareStatement(sql);
			stm.setString(1, category);
			rs = stm.executeQuery();
			while(rs.next()){
				bookIdList.add(rs.getString("id"));
			}
		} catch (SQLException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}finally{
			this.closeConnection(conn, stm, rs);
		}
		
		// TODO Auto-generated method stub
		return bookIdList;
	}


}
