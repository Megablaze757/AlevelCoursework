from pyscript import document



def handle_submit(event=None): 
  
    #Access the HTML element for the username
    username_element = document.querySelector("#Username")
    password_element = document.querySelector("#Password")
    
   # Assign the form value to the username variable 
    username = username_el.value
    
    
    print(username)
