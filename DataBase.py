import sqlite3
if __name__!="__main__":

    Con=sqlite3.connect("Uploader.Db",check_same_thread=False)

    Con.cursor().execute("CREATE TABLE IF NOT EXISTS Admin( [Id] INTEGER PRIMARY KEY NOT NULL, [Firstname] NVARCHAR(100) NOT NULL , [Acssess] INTEGER DEFAULT 0)").close()
    Con.cursor().execute("CREATE TABLE IF NOT EXISTS User( [Id] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, [UserId] INTEGER NOT NULL , [Firstname] NVARCHAR(100) NOT NULL)").close()
    Con.cursor().execute("CREATE TABLE IF NOT EXISTS LocksLink ([Link] NVARCHAR(800) PRIMARY KEY NOT NULL , [Title] NVARCHAR(50) NOT NULL , [TextLink] NVARCHAR(800) DEFAULT NULL)").close()

    def InsertAdmin(id:int,firstname:str,accsess=1)->int:
        """New Admin"""
        try:
            if type(id)==int and type(firstname)==str and not(firstname is None and firstname == ""):
                Values=(id,firstname,accsess)
                Result=Con.cursor().execute("INSERT INTO Admin VALUES(?,?,?)",Values).rowcount
                Con.commit()
                if Result==1:
                    return 200
                return 500
        except Exception as e:
            return 500
    
    def DeleteAdmin(id:int)->int:
        "Delete Admin"
        try:
            if type(id)==int:
                Result=Con.cursor().execute("DELETE FROM Admin WHERE Id=%s"%id).rowcount
                Con.commit()
                if Result==None:
                    return 404
                if Result>=0:
                    return 200
                return 500
        except Exception as e:
            return 500

    def InsertUser(userid:int,firstname:str)->int:
        "New User"
        try:
            if type(userid)==int and type(firstname)==str and not(firstname is None and firstname == ""):
                Values=(userid,firstname)
                Result=Con.cursor().execute("INSERT INTO User VALUES(NULL,?,?)",Values).rowcount
                Con.commit()
                if Result==1:
                    return 200
                return 500
        except Exception as e:
            return 500

    def AnyAdmin(id:int)->int:
        "Exist Admin"
        try:
            if type(id)==int:
                Result=Con.cursor().execute("SELECT Acssess FROM Admin WHERE Id=%s"%id).fetchone()
                Con.commit()
                if Result==None or len(Result)==0:
                    return 404
                if len(Result)==1:
                    return (200,Result)
                return 500
        except Exception as e:
            return 500
        
    def AnyUser(id:int)->int:
        "Exist Admin"
        try:
            if type(id)==int:
                Result=Con.cursor().execute("SELECT * FROM User WHERE UserId=%s"%id).fetchone()
                Con.commit()
                if Result==None or len(Result)==0:
                    return 404
                if len(Result)==1:
                    return (200,Result)
                return 500
        except Exception as e:
            return 500
        
    def InfoAdmin(id:int)->tuple:
        "Get Admins"
        try:
                Result=Con.cursor().execute("SELECT * FROM Admin WHERE Id=%s"%id).fetchone()
                Con.commit()
                if Result==None or len(Result)==0:
                    return 404
                if Result!=None and len(Result)>0:
                    return Result
                return 500
        except Exception as e:
            return 500
    
    def InsertLocksLink(userlink:str,title:str,linktext)->int:
        "New Link"
        try:
            if type(userlink)==str:
                Result=Con.cursor().execute("INSERT INTO LocksLink VALUES(?,?,?)",(userlink,title,linktext)).rowcount
                Con.commit()
                if Result==1:
                    return 200
                return 500
        except Exception as e:
            return 500
        
    def DeleteLocksLink(userlink:str)->int:
        "Delete Link"
        try:
            if type(userlink)==str:
                Result=Con.cursor().execute("Delete From LocksLink Where Link='%s'"%userlink).rowcount
                Con.commit()
                if Result==1:
                    return 200
                return 500
        except Exception as e:
            return 500
  
    def FetchLocksLink()->int:
        "Select Link"
        try:
            Result=Con.cursor().execute("Select * from LocksLink").fetchall()
            Con.commit()
            if len(Result)>0:
                return Result
            return Result
        except Exception as e:
            return 500
        
    def FetchUsers()->int:
        "Select Users"
        try:
            Result=Con.cursor().execute("Select * from User").fetchall()
            Con.commit()
            if len(Result)>0:
                return Result
            return Result
        except Exception as e:
            return 500
        
    