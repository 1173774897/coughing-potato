package dao;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

public class BaseDao {
    static String driver = "com.mysql.jdbc.Driver";
    static String url = "jdbc:mysql://127.0.0.1:3306/DoubanBook?useUnicode=true&characterEncoding=utf-8&useSSL=false";
    static String user = "root";
    static String password = "lizoe";
    
    public static Connection getConnection(){
    	Connection connection = null;
    	try{
    		Class.forName(driver);
    		connection = DriverManager.getConnection(url,user,password);
    		
    	}
    	catch(ClassNotFoundException e){
    		System.out.println("can not find the driver");
    		e.printStackTrace();
    	}catch(SQLException e){
    		e.printStackTrace();
    	}catch(Exception e){
    		e.printStackTrace();
    	}
    	return connection;
    }
    
    public void closeConnection(Connection connection, Statement st, ResultSet rs){
    	try{
    		if(connection != null){
    			connection.close();
    		}
    		if(st != null){
    			st.close();
    		}
    		if(rs != null){
    			rs.close();
    		}
    	}
    	catch(SQLException e){
    		e.printStackTrace();
    	}
    }
}
