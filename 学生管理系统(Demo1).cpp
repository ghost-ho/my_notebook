#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <Windows.h>
#include <ctime>
#include "Student.cpp"

static void init()
{
	std::cout << "            欢迎使用学生管理系统!      " << "\n";
	std::cout << "====================================" << "\n";
	std::cout << "            1. 注册学生管理系统" << "\n";
	std::cout << "            2. 登录学生管理系统" << "\n";
	std::cout << "            3. 增加新的学生" << "\n";
	std::cout << "            4. 删除学籍记录" << "\n";
	std::cout << "            5. 修改学生信息" << "\n";
	std::cout << "            6. 查找学生信息" << "\n";
	std::cout << "            7. 关于本系统" << "\n";
	std::cout << "            8. 退出系统" << "\n";
	std::cout << "====================================" << "\n";
}

static void about(std::string command)
{
	system("cls");
	if (command == "7")
	{
		std::cout << "当前版本: 1.0" << "\n";
		std::cout << "本系统由 cyan_Alice 独立编写." << "\n";
		Sleep(500);
	}
}

static bool EXIT(std::string command)
{
	if (command == "8")
	{
		return false;
	}
	else
	{
		return true;
	}
}



Student AddStudent(std::string STUDENT_NAME, unsigned int STUDENT_AGE, unsigned int STUDENT_CLASS, unsigned int STUDENT_GRADE, std::string STUDENT_ID)
{
	Student student;
	student.studentName = STUDENT_NAME;
	student.studentAge = STUDENT_AGE;
	student.studentClass = STUDENT_CLASS;
	student.studentGrade = STUDENT_GRADE;
	student.studentId = STUDENT_ID;
	return student;
}


// 学生序列
std::vector<Student> Students = {};



int main()
{
	std::string command = "";

	while (EXIT(command))
	{
		init();
		std::cin >> command;
		if (command == "7")
		{
			about(command);
		}
	}


}