from django import forms
from django.contrib.auth.models import User
from . import models
from django.db.models import Q

class IssueBookForm(forms.Form):
   
    name2 = forms.ModelChoiceField(queryset= models.Student.objects.all(), empty_label="", to_field_name="user", label="Student Details")
    
    
    name2.widget.attrs.update({'class':'form-control'})
    def __init__(self, *args, **kwargs):
        super(IssueBookForm, self).__init__(*args, **kwargs)
        ib = models.IssuedBook.objects.only('isbn')
        l1= []
        for x in ib:
            l1.append(x.isbn)  
        self.fields['isbn2']  = forms.ModelChoiceField(queryset= models.Book.objects.filter(~Q(isbn__in=l1)), empty_label="", to_field_name="isbn", label="Book (Name and ISBN)")
        
       