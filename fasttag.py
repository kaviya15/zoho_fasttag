import time
models_rate = {
"car":85,
"jeep":85,
"van":85,
"lcv":135,
"bus":285,
"track":285,
"1-3axlevehicle":315,
"4-6axlevehicle":450,
"hcm":450,
"eme":450,
"above7axle":550
}
class users:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class fastag:
    def __init__(self):
        self.root = None
    def key(self,value):
        num = ""
        for i in value:
            num+=str(ord(i))
        return int(num)
    def find_user(self,value):
        keyvalue = self.key(value)
        value_data = None
        if self.root == None:
            return(value_data)
        else:
            def get_user(node):
                if node.value["key_value"] == keyvalue:
                    end = time.time()
                    nonlocal value_data
                    value_data = node.value
                    value_data["endtime"] = end
                    return (value_data)
                elif node.left!=None and keyvalue< node.value["key_value"]:
                    get_user(node.left)
                elif  node.right!=None and keyvalue > node.value["key_value"]:
                    get_user(node.right)
            get_user(self.root)
            return (value_data)

    def register_user(self,value):
        value["key_value"] = self.key(value["key"])
        node = users(value)
        node.value["model"] = node.value["model"].lower()
        if self.root == None:
            node.value["starttime"] = time.time()
            print(node.value)
            self.root = node
        else:
            def find_node(node_node):
                if node.value["key_value"]< node_node.value["key_value"]:
                    if node_node.left == None:
                        node.value["starttime"] = time.time()
                        node_node.left = node
                    else:
                        find_node(node_node.left)
                elif node.value["key_value"] > node_node.value["key_value"]:
                    if node_node.right==None:
                        node.value["starttime"] = time.time()
                        node_node.right = node
                    else:
                        find_node(node_node.right)
            find_node(self.root)
        return(node.value)
    def charges(self,model):
        print(model["model"])
        if model["model"][0:1].isalpha():
            return (models_rate[model["model"]])
        elif int(model["model"][0:1])> 0 and int(model["model"][0:1]) <= 3 and model["model"][1:] == "axlevehicle":
                return(models_rate["1-3axlevehicle"])
        elif int(model["model"][0:1])>=4 and int(model["model"][0:1])<=6 and model["model"][1:] == "axlevehicle":
                return (models_rate["4-6axlevehicle"] )
        elif int(model["model"][0:1])>=7 and model["model"][1:] == "axlevehicle":
                return (models_rate["above7axle"] )
        else:
            print("No such model found")

    def billAmount(self,new_one,model):
        print(model["model"])
        if new_one == True:
            charge = self.charges(model)
            print("Total bill = " , charge+50,"// Current toll fare" , charge, "+ 50 registration fee")

        else:
            # print(model["endtime"],model["starttime"])
            hours, rem = divmod(model["endtime"] - model["starttime"], 3600)
            minutes, seconds = divmod(rem, 60)
            # print(minutes)
            if minutes<=30:
                print("Total bill=",self.charges(model)/2)
            elif minutes>30:
                print("Total bill=",self.charges(model))
user1 = fastag()
# user1.register_user(obj2)
vehicle_number = input().split(' ')
veh_num = ""
for i in vehicle_number:
    if i == " ":
        continue
    else:
        veh_num += i
user_data = user1.find_user(veh_num.upper())
if user_data ==None:
     print("Vehicle number you entered does not have fast tag")
     print("Choose 1 to Register for fast tag""\n""Choose 2 to exit")
     choice = int(input("Enter your option"))
     if choice==1:
         usr_data = user1.register_user({
             "name": input(" Enter owner name: "),
             "key": veh_num.upper(),
             "model":input("Enter vehicle Type: ")
             })
         print(usr_data)
         user1.billAmount(True,usr_data)

elif user_data["key"] == veh_num:
    user1.billAmount(False,user_data)
