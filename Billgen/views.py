from django.shortcuts import render, get_object_or_404, redirect
from .models import ItemList
from .forms import AddItemForm
# Create your views here.

def ItemListView(request):
    queryset = ItemList.objects.all()
    my_context = {
        'object': queryset
    }
    return render(request, "ItemList.html", my_context)

def SelectAction(request):
        if request.method == 'POST' and 'add' in request.POST:
            form = AddItemForm()
            print(form.errors)
            return render(request, "createItem.html",{'form':form})
        else:
            form = AddItemForm(request.POST or None)
            if form.is_valid():
                print(form.cleaned_data)
                ItemList.objects.create(**form.cleaned_data)
                return redirect("/./home/")

        if 'remove' in request.POST:
            it_list = request.POST.getlist('frt')
            queryset = ItemList.objects.all()
            if it_list :
                for item in it_list:
                    obj = get_object_or_404(ItemList, sno = item )
                    obj.delete()
                return redirect('/./home/')
            else:
                return render(request, "ItemList.html", {'object': queryset})

        if 'bill' in request.POST:
            query =  []
            it_list = request.POST.getlist('frt')
            queryset = ItemList.objects.all()
            if it_list:
                for itm in it_list:
                    query.append(ItemList.objects.get(sno= itm))

                if len(query) > 1:
                    total = 0
                    for i in range(0, len(query)):
                        amnt = int(query[i].amount)
                        total +=  amnt

                    return render(request, "ItemList.html", {'obj': query,'object': queryset,'total':total})
                else:
                    return render(request, "ItemList.html", {'obj': query, 'object': queryset})
            else:
                return render(request, "ItemList.html",{'object': queryset})

def MultiItem(request):
    queryset = ItemList.objects.all()
    query = []
    total = []
    count = amnt = 0
    if request.method == 'POST':
        entry = request.POST.getlist('entry')
        for i in range(0,len(entry)):
            if entry[i]:
                q = []
                count = count + 1
                q.append(queryset[i])
                if len(entry[i]) > 1:
                    enl = entry[i].split(',')

                    for l in enl:
                        if l != str(queryset[i].sno):
                            q.append(ItemList.objects.get(sno = int(l)))

                elif entry[i] != str(queryset[i].sno):
                    q.append(ItemList.objects.get(sno=int(entry[i])))
                query.append(q)

        # print(query)
        for ir in query:
            amnt = 0
            for j in ir:
                amnt += int(j.amount)
            total.append(amnt)

        my_context = {
            'object': queryset,
            'query': query,
            'total': total[::-1],
            'count': range(0,len(query)-1)
        }
        # return render(request, "multiItemSelect.html", my_context)

    else:
        my_context = {
            'object': queryset,
        }
    return render(request, "multiItemSelect.html", my_context)
