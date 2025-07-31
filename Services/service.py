from flask import Flask,request,jsonify
import re,json,os,platform,sys
from flask_cors import CORS, cross_origin
from datetime import datetime
from config import connect



def CreateProject(data):
  
    try:
        print(data)
        ProjectForm = data["ProjectForm"]
        ProjectName = ProjectForm["ProjectName"]
        ProjectLocation = ProjectForm["ProjectLocation"]
        # ProjectPath = ProjectForm["ProjectImage"]
        StartDate = ProjectForm["StartDate"]
        EndDate = ProjectForm["EndDate"]
        image = data["image"]
        
        Date = datetime.now()
        print("--->>",Date)
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO tbl_ProjectList(ProjectName, ProjectLocation, ProjectPath, StartDate, EndDate, CreatedBy, CreatedOn ) Values ('{ProjectName}','{ProjectLocation}','{image}','{StartDate}','{EndDate}','admin','{Date}')"
        )
        conn.commit()
        return ProjectForm
  
    except Exception as e:
         print(e)


def FetchProject():
  
    try:

        conn = connect()
        cur = conn.cursor()
        cur.execute(
            f"Select Id,projectname, projectpath from tbl_ProjectList order by 1 asc"
        )
        # response = cur.fetchall()
        # print(response)
        columns = cur.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
        print(result)
        return result
  
    except Exception as e:
         print(e)

def FetchProjectDetails(data):
  
    try:
        print(data)
        projectId=data['id']
        print(projectId)
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            f"Select * from tbl_ProjectList where id={projectId} order by 1 asc"
        )
        # response = cur.fetchall()
        # print(response)
        columns = cur.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
        print(result)
        return result
  
    except Exception as e:
         print(e)

def CreateTask(data):
  
    try:
        print(data)
        TaskForm = data["TaskForm"]
        TaskName = TaskForm["TaskName"]
        ProjectId = TaskForm["ProjectId"]
        StageId = TaskForm["StageId"]
        IsCompleted = TaskForm["IsCompleted"]
   
        
        Date = datetime.now()
        print("--->>",Date)
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO tbl_tasklist(TaskName, ProjectId, StageId, IsCompleted, CreatedBy, CreatedOn ) Values ('{TaskName}','{ProjectId}','{StageId}','{IsCompleted}','admin','{Date}')"
        )
        conn.commit()
        return TaskForm
  
    except Exception as e:
         print(e)


def CreateStage(data):
  
    try:
        print(data)
        StageForm = data["StageForm"]
        StageName = StageForm["StageName"]
        ProjectId = StageForm["ProjectId"]
        IsCompleted = StageForm["IsCompleted"]
   
        
        Date = datetime.now()
        print("--->>",Date)
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            f"INSERT INTO tbl_stagelist(StageName, ProjectId, IsCompleted, CreatedBy, CreatedOn ) Values ('{StageName}','{ProjectId}','{IsCompleted}','admin','{Date}')"
        )
        conn.commit()
        return StageForm
  
    except Exception as e:
         print(e)


def FetchProjectDetails(data):
  
    try:
        print(data)
        projectId=data['id']
        print(projectId)
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            f"Select * from tbl_ProjectList where id={projectId} order by 1 asc"
        )   
        # response = cur.fetchall()
        # print(response)
        columns = cur.description 
        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in cur.fetchall()]
        print(result)
        return result
  
    except Exception as e:
         print(e)

def SearchProject(data):
  
    try:
        print(data)
        searchprjct = data["SearchTerm"]
   
   
        
 
        conn = connect()
        cur = conn.cursor()
        cur.execute(
            f"select ProjectName from tbl_projectlist where ProjectName LIKE '%{searchprjct}%'"
        )
        SearchProjectList = cur.fetchall()
        conn.commit()
        return SearchProjectList
  
    except Exception as e:
         print(e)
 