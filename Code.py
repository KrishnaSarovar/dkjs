# # Assignment No: 5 
 
# # Title: Perform white box testing to calculate cyclomatic complexity of program.  
 
# # Source code:   
# #  import unittest 
 
# # def sample_function(x, y): 
# #     if x > 0: 
# #         if y > 0: 
# #             return x + y 
# #         else: 
# #             return x - y 
# #     else: 
# #         if y > 0: 
# #             return y - x 
# #         else: 
# #             return x * y 
 
 
# # class TestSampleFunction(unittest.TestCase): 
 
# #     def test_positive_numbers(self): 
# #         self.assertEqual(sample_function(2, 3), 5) 
 
# #     def test_negative_y(self): 
# #         self.assertEqual(sample_function(2, -3), 5) 
 
# #     def test_negative_x(self): 
# #         self.assertEqual(sample_function(-2, 3), 5) 
 
# #     def test_both_negative(self): 
# #         self.assertEqual(sample_function(-2, -3), 6) 
 
 
# # def run_tests(): 
# #     loader = unittest.TestLoader() 
# #     suite = loader.loadTestsFromTestCase(TestSampleFunction) 
 
# #     runner = unittest.TextTestRunner(verbosity=2) 
# #     result = runner.run(suite) 
 
# #     if result.wasSuccessful(): 
# #         print("\nAll tests executed successfully!") 
# #     else: 
# #         print("\nSome tests failed. Check the output above for details.") 
 
 
# # if __name__ == "__main__": 
# #     run_tests()
# # Krishna Mansaram Sarovar
# # 25MC15P08F
# # Output:-
# # ________________________________________________________________________________________
# Assignment no :6 
# Title: Perform white box testing to test all possible execution path in program. (Control 
# Flow) 
# Source Code: 
# def is_prime(n): 
# if n <= 1: 
# print(f"{n} is not a prime number.") 
# return False 
# elif n == 2: 
# print(f"{n} is a prime number.") 
# return True 
# elif n % 2 == 0: 
# print(f"{n} is not a prime number.") 
# return False 
# else: 
# for i in range(3, int(n**0.5) + 1, 2): 
# if n % i == 0: 
# print(f"{n} is not a prime number.") 
# return False 
# print(f"{n} is a prime number.") 
# return True 
# test_numbers = [1, 2, 3, 4, 5, 9, 11, 15, 17, 19] 
# for number in test_numbers: 
# print(f"Testing {number}:") 
# is_prime(number) 
# print("-" * 30) 
# print("All tests have been completed successfully.")
# _________________________________________________________________________________________

# Assignment No: 7 
# Title: Perform white box testing to analys and test the flow of data within program by 
# tracking variable definition, uses and variable life cycle. (Data Flow) 
# Source Code: 
# import sys 
# def min_key(key,mst_set,vertices): 
# min_value = sys.maxsize 
# min_index = -1 
# for v in range (vertices): 
# if key[v]< min_value and not mst_set[v]: 
# min_index = key[v] 
# min_index = v 
# return min_index 
# def prim(graph, vertices): 
# key = [sys.maxsize] * vertices 
# parent = [-1]* vertices 
# key[0]=0 
# mst_set = [False] * vertices 
# for _ in range(vertices): 
# u = min_key(key, mst_set, vertices) 
# mst_set[u] = True 
# for v in range(vertices): 
# if graph[u][v] and not mst_set[v] and graph[u][v] <key[v]: 
# key[v] 
# key[v] = graph[u][v] 
# return parent 
# def print_mst(parent, graph, vertices): 
# print("Minimum Spanning Tree (MST):") 
# for i in range(1, vertices): 
# print(f"Edge: {parent[i]} - {i}, Weight: {graph[i][parent[i]]}") 
# print("\nMST Construction Successful!") 
# graph=[ 
# [0,2,0,6,0], 
# [2,0,3,8,5], 
# [0,3,0,0,7], 
# [6,8,0,0,9], 
# [9,5,7,9,0] 
# ] 
# vertices = len(graph) 
# parent = prim(graph,vertices) 
# print_mst(parent,graph,vertices) 
# print("\n Overall process completed successfully!")

# _________________________________________________________________________________________

# Assignment: 8 
# Title: Perform Black Box Testing Using a Testing Tool On An Application Testing Point 
# To Be Covered Data-Driven Wizard, Parameterization, and Exception Handling. 
# Source Code: 
# from os import name

# from selenium import webdriver 
# from selenium.webdriver.common.by import By 
# from selenium.webdriver.support.ui import WebDriverWait 
# from selenium.webdriver.support import expected_conditions as EC 
# import unittest 
# import time 
# class TestControlFlow(unittest.TestCase): 
# def setUp(self): 
# options = webdriver.ChromeOptions() 
# options.add_experimental_option("detach", True) 
# self.driver = webdriver.Chrome(options=options) 
# self.wait = WebDriverWait(self.driver, 15) 
# self.test_data = [ 
# { 
# "username": 
# "
# Krishn
# 381@gmail.com@gmail.com"
# , "password": "
# Krishnasarovar
# @2206", 
# "expected": "success" 
# }, 
# { 
# } 
# ] 
# "username": "invalid_user", 
# "password": "invalid_password", 
# "expected": "failure" 
# def test_login(self): 
# driver = self.driver 
# for data in self.test_data: 
# with self.subTest(username=data['username'], password=data['password']): 
# try: 
# driver.get("https://mymatoshri.edupluscampus.com/") 
# time.sleep(3) 
# inputs = driver.find_elements(By.TAG_NAME, "input") 
# print(f"{len(inputs)} input fields found") 
# if len(inputs) < 2: 
# self.fail("Not enough input fields found on the page") 
# inputs[0].clear() 
# inputs[0].send_keys(data['username']) 
# print(f"Username Entered: {data['username']}") 
# time.sleep(1) 
# inputs[1].clear() 
# inputs[1].send_keys(data['password']) 
# print(f"Password Entered: {data['password']}") 
# time.sleep(1) 
# login_button = self.wait.until( 
# EC.element_to_be_clickable( 
# (By.XPATH, "//button[@type='submit']") 
# ) 
# ) 
# login_button.click() 
# print("Login Button Clicked!") 
# time.sleep(5) 
# current_url = driver.current_url 
# if data['expected'] == "success": 
# print("Login Successful!") 
# if "Dashboard" in current_url: 
# print("Dashboard Validation Passed") 
# else: 
# print("Dashboard Validation Failed") 
# self.fail("Expected to see Dashboard but did not") 
# elif data['expected'] == "failure": 
# print("Login Failed as Expected!") 
# if "Dashboard" in current_url: 
# self.fail("Invalid credentials logged in successfully (unexpected)") 
# except Exception as e: 
# print(f"Error Occurred: {e}") 
# self.fail(f"Test Failed: {e}") 
# def tearDown(self): 
# self.driver.quit() 
# if  name == " main ":
#     unittest.main()

# _________________________________________________________________________________________

# Assignment No: 9 
# Title: Test Automation For Checkbox Selection And State Verification Using 
# Selenium. 
# Source Code: 
# CountCheckbox.java 
# import org.openqa.selenium.By; 
# import org.openqa.selenium.WebDriver; 
# import org.openqa.selenium.WebElement; 
# import org.openqa.selenium.chrome.ChromeDriver; 
# import java.util.List; 
# public class CountCheckboxes { 
# public static void main(String[] args) throws InterruptedException { 
# WebDriver driver = new ChromeDriver(); 
# driver.get("file:///C:/Users/Admin/Desktop/Himanshu/ass 9-10/index.html"); 
# List<WebElement> checkboxes = 
# driver.findElements(By.xpath("//input[@type='checkbox']")); 
# for (int i = 0; i < checkboxes.size(); i += 2) { 
# checkboxes.get(i).click(); 
# } 
# int checked = 0, unchecked = 0; 
# for (int i = 0; i < checkboxes.size(); i++) { 
# boolean status = checkboxes.get(i).isSelected(); 
# System.out.println("Checkbox " + (i + 1) + ": " + status); 
# if (status) checked++; 
# else unchecked++; 
# } 
# System.out.println("Selected: " + checked); 
# System.out.println("Unselected: " + unchecked); 
# Thread.sleep(60000); 
# driver.quit();

# } 
# } 
# Index.html 
# <!DOCTYPE html> 
# <html lang="en"> 
# <head> 
# <meta charset="UTF-8"> 
# <meta name="viewport" content="width=device-width, initial-scale=1.0"> 
# <title>Student Course Registration</title> 
# <style> 
# *{ 
# margin:0; 
# padding:0; 
# box-sizing:border-box; 
# } 
# body{ 
# font-family:Arial,sans-serif; 
# background:linear-gradient(135deg,#74ebd5,#ACB6E5); 
# height:100vh; 
# display:flex; 
# justify-content:center; 
# align-items:center; 
# } 
# .container{ 
# width:400px; 
# background:white; 
# padding:30px; 
# border-radius:15px; 
# box-shadow:0px 8px 20px rgba(0,0,0,0.3); 
# } 
# h2{ 
# text-align:center; 
# color:#2c3e50; 
# margin-bottom:20px; 
# } 
# .input-box{ 
# margin-bottom:15px; 
# } 
# label{ 
# font-weight:bold; 
# display:block; 
# margin-bottom:5px; 
# } 
# input[type=text], 
# input[type=password]{ 
# width:100%; 
# padding:10px; 
# border-radius:8px; 
# border:1px solid gray; 
# } 
# .courses label{ 
# display:block; 
# margin:10px 0; 
# } 
# .btn{ 
# width:100%; 
# padding:12px; 
# background:#3498db; 
# border:none; 
# border-radius:8px; 
# color:white; 
# font-size:16px; 
# cursor:pointer; 
# } 
# .btn:hover{ 
# background:#21618c; 
# } 
# .footer{ 
# margin-top:15px; 
# text-align:center; 
# color:gray; 
# } 
# </style> 
# </head> 
# <body> 
# <div class="container"> 
# <h2>Student Course Registration</h2> 
# <form> 
# <div class="input-box"> 
# <label>Username</label> 
# <input id="username" type="text" 
# placeholder="Enter username"> 
# </div> 
# <div class="input-box"> 
# <label>Password</label> 
# <input id="password" type="password" 
# placeholder="Enter password"> 
# </div> 
# <div class="courses"> 
# <label> 
# <input type="checkbox" id="c1"> 
# Java 
# </label> 
# <label> 
# <input type="checkbox" id="c2"> 
# Python 
# </label> 
# <label> 
# <input type="checkbox" id="c3"> 
# Machine Learning 
# </label> 
# <label> 
# <input type="checkbox" id="c4"> 
# Generative AI 
# </label> 
# <label> 
# <input type="checkbox" id="c5"> 
# Power BI 
# </label> 
# </div> 
# <button class="btn"> 
# Register 
# </button> 
# </form> 
# <div class="footer"> 
# Learn Today, Lead Tomorrow 🚀 
# </div> 
# </div> 
# </body> 
# </html>

# _________________________________________________________________________________________

# Assignment: 10 
# Title: Test Automation For Checkbox Selection And State Verification for Links Using 
# Selenium. 
# Source Code: 
# CountLink.java 
# import org.openqa.selenium.By; 
# import org.openqa.selenium.WebDriver; 
# import org.openqa.selenium.WebElement; 
# import org.openqa.selenium.chrome.ChromeDriver; 
# import java.util.List; 
# public class CountLinks { 
# public static void main(String[] args) throws InterruptedException { 
# WebDriver driver = new ChromeDriver(); 
# driver.get(" file:///C:/Users/Admin/Desktop/Himanshu/ass 9-10/Links.html "); 
# List<WebElement> linksCount = 
# driver.findElements(By.tagName("a")); 
# System.out.println("Total number of links: " + linksCount.size()); 
# System.out.println("\nThe names of the links are as follows:"); 
# for (int i = 0; i < linksCount.size(); i++) { 
# System.out.println("Link number " + (i + 1) + " : " 
# + linksCount.get(i).getText()); 
# } 
# Thread.sleep(60000); 
# driver.quit(); 
# } 
# Links.html 
# <!DOCTYPE html> 
# <html> 
# <head> 
# <title>Educational & Tech Links</title> 
# <style> 
# body{ 
# font-family: Arial,sans-serif; 
# background:linear-gradient(to right,#00c6ff,#0072ff); 
# text-align:center; 
# padding-top:50px; 
# } 
# .box{ 
# background:white; 
# width:350px; 
# margin:auto; 
# padding:25px; 
# border-radius:15px; 
# box-shadow:0px 8px 20px rgba(0,0,0,0.3); 
# } 
# h2{ 
# margin-bottom:20px; 
# color:#2c3e50; 
# } 
# a{ 
# display:block; 
# text-decoration:none; 
# padding:12px; 
# margin:10px 0; 
# border-radius:8px; 
# font-size:16px; 
# font-weight:bold; 
# background:linear-gradient(to right,#8e2de2,#4a00e0); 
# color:white; 
# transition:0.3s; 
# } 
# a:hover{ 
# transform:scale(1.05); 
# background:linear-gradient(to right,#11998e,#38ef7d); 
# } 
# </style> 
# </head> 
# <body> 
# <div class="box"> 
# <h2>Learning & Career Links</h2> 
# <a href="https://www.google.com" target="_blank"> 
# Google 
# </a> 
# <a href="https://www.github.com" target="_blank"> 
# GitHub 
# </a> 
# <a href="https://www.geeksforgeeks.org" target="_blank"> 
# GeeksforGeeks 
# </a> 
# <a href="https://www.w3schools.com" target="_blank"> 
# W3Schools 
# </a> 
# <a href="https://www.stackoverflow.com" target="_blank"> 
# Stack Overflow 
# </a> 
# </div> 
# </body> 
# </html> 