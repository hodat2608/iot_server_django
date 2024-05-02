from django.shortcuts import render
from server.models import server_test
from A18_RS656.models import A18,category
from django.http import JsonResponse

def detail_date(request,id):
    date = A18.objects.filter(client_id = id).order_by('-id')[:10]
    name_space_id = server_test.objects.get(id=id)
    name_space = name_space_id.name_client
    context = {'date': date,'name_space':name_space}
    return render(request, 'static/A18/index_date.html', context)

def chart_date(request, id):
    date = A18.objects.filter(client_id=id).order_by('-id')[:10]
    dat_and_last_records = []
    for dat in date:
        last_category_record = dat.category_set.order_by('id').last()
        # category_lddk_records = dat.category_lddk_set.all()
        # lddk_records_data = [{'tong_pp_pdn': record.tong_pp_pdn} for record in category_lddk_records]
        if last_category_record:
            last_record_data = {
                'tong_so_luong_sx': last_category_record.tong_so_luong_sx,
                'tong_so_luong_pp': last_category_record.tong_so_luong_pp,
            }
        else:
            last_record_data = None
        dat_and_last_records.append({'date_on_excel': dat.date_on_excel,'lot': dat.lot, 'last_record': last_record_data,})
    return JsonResponse({'dat_and_last_records': dat_and_last_records})

def detail_data(request,id):
    data = category.objects.filter(date_id = id)
    context = {'data': data, 'name_space':'ccai0019','date_id': id}
    return render(request, 'static/A18/index_data_realtime.html', context)

def detail_data_realtime(request, id):
    data = category.objects.filter(date_id=id)
    serialized_data = [{'date_id': entry.date_id,
                        'ngay_san_xuat': entry.ngay_san_xuat[:10],
                        'gio_luu_du_lieu': entry.gio_luu_du_lieu,
                        'tong_so_luong_sx': entry.tong_so_luong_sx,
                        'cuon_cam': entry.cuon_cam,
                        'cacbon_tay_choi': entry.cacbon_tay_choi,
                        'han_choi': entry.han_choi,
                        'han_chau': entry.han_chau,
                        'de_vo_nho': entry.de_vo_nho,
                        'tu_dien': entry.tu_dien,
                        'cong_chau_dien': entry.cong_chau_dien,
                        'bui_chi': entry.bui_chi,
                        'phe_pham_khac': entry.phe_pham_khac,
                        'tong_so_luong_pp': entry.tong_so_luong_pp} for entry in data]
    return JsonResponse(serialized_data, safe=False)

def chart_data_realtime(request, id):
    last_entry = category.objects.filter(date_id=id).order_by('-id').first()
    last_entry_data = {
                        'date_id': last_entry.date_id,
                        'ngay_san_xuat': last_entry.ngay_san_xuat[:10],
                        'gio_luu_du_lieu': last_entry.gio_luu_du_lieu,
                        'tong_so_luong_sx': last_entry.tong_so_luong_sx,
                        'cuon_cam': last_entry.cuon_cam,
                        'cacbon_tay_choi': last_entry.cacbon_tay_choi,
                        'han_choi': last_entry.han_choi,
                        'han_chau': last_entry.han_chau,
                        'de_vo_nho': last_entry.de_vo_nho,
                        'tu_dien': last_entry.tu_dien,
                        'cong_chau_dien': last_entry.cong_chau_dien,
                        'bui_chi': last_entry.bui_chi,
                        'phe_pham_khac': last_entry.phe_pham_khac,
                        'tong_so_luong_pp': last_entry.tong_so_luong_pp
                        }
    print(last_entry_data)
    return JsonResponse(last_entry_data, safe=False)

def search_date_lot(request):
    if request.method == 'GET':
        query = request.GET.get('query')  
        if query.strip() != '':
            search_date = A18.objects.filter(date_on_excel__icontains=query)
            result = []
            for date in search_date:
                result.append({'date': date.date_on_excel,'lot':date.lot,'id_date_url':f'/detail/ccai0019_detail_data/{date.id}/' }) 
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse([])
        
def delete_selected_records(request):
    if request.method == "POST" and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        selected_ids = request.POST.getlist("selectedIds[]")
        A18.objects.filter(id__in=selected_ids).delete()
        return JsonResponse({"message": "Selected records deleted successfully."})
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)
