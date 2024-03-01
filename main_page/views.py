from django.shortcuts import render
from json import dumps

# Create your views here.

def home(request) :
    if request.method == 'POST' :
        classes_attended = request.POST['classes_attended']
        classes_held = request.POST['classes_held']
        

    
        
        classes_attended=int(classes_attended)
        classes_held = int(classes_held)

        attendance_percentage =int((classes_attended) / (classes_held) * 100)
        current_attendance =  (classes_attended) / (classes_held) 


        required_attendance = 0.75 
        remaining_classes = classes_held
        classes_attended = current_attendance * classes_held
            
        while (int(classes_attended) / int(remaining_classes))  < required_attendance:
            remaining_classes += 1
            classes_attended += 1
            
        need_to_attend=remaining_classes - classes_held

        class_data=[]
        class_data.extend([classes_attended,classes_held,attendance_percentage,need_to_attend])
        print(class_data)
        class_data=dumps(class_data)

        context = {
                    "classes_attended":classes_attended,
                   "classes_held":classes_held,
                "attendance_percentage":attendance_percentage ,
                "need_to_attend":need_to_attend,
                "class_data" : class_data

                }
        return render(request, 'forms.html',context)
    return render(request, 'forms.html')

