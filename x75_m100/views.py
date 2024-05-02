from django.shortcuts import render,redirect
from x75_m100.models import x75,category
from server.models import server_test 
from x75_m100.models import category_lddk
from django.http import StreamingHttpResponse
from django.http import JsonResponse
import json

def chart_date(request, id):
    date = x75.objects.filter(client_id=id).order_by('-id')[:10]
    dat_and_last_records = []
    for dat in date:
        last_category_record = dat.category_set.order_by('id').last()
        category_lddk_records = dat.category_lddk_set.all()
        lddk_records_data = [{'tong_pp_pdn': record.tong_pp_pdn} for record in category_lddk_records]
        if last_category_record:
            last_record_data = {
                'tong_sl_sx': last_category_record.tong_sl_sx,
                'tong_sl_pp_kx': last_category_record.tong_sl_pp_kx,
            }
        else:
            last_record_data = None
        dat_and_last_records.append({'date_on_excel': dat.date_on_excel,'lot': dat.lot, 'last_record': last_record_data,'lddk_records':lddk_records_data})
    return JsonResponse({'dat_and_last_records': dat_and_last_records})

def detail_date(request,id):
    date = x75.objects.filter(client_id = id).order_by('-id')[:10]
    name_space_id = server_test.objects.get(id=id)
    name_space = name_space_id.name_client
    context = {'date': date,'name_space':name_space}
    return render(request, 'static/X75/index_date.html', context)

def detail_date_show_all(request,id):
    date = x75.objects.filter(client_id = id)
    name_space_id = server_test.objects.get(id=id)
    name_space = name_space_id.name_client
    print(name_space)
    context = {'date': date,'name_space':name_space}
    return render(request, 'static/X75/index_date_show_all.html', context)

def detail_data(request,id):
    data = category.objects.filter(date_id = id)
    try:
        data_lddk = category_lddk.objects.get(date_1_id=id)
    except category_lddk.DoesNotExist:
        data_lddk = category_lddk.objects.create(date_1_id=id)  
        data_lddk.save()
    context = {'data': data, 'name_space':'ccai0015','date_id': id,'data_lddk':data_lddk}
    return render(request, 'static/X75/index_data_realtime.html', context)


def detail_data_realtime(request, id):
    data = category.objects.filter(date_id=id)
    serialized_data = [{'date_id': entry.date_id,
                        'ngay_san_xuat': entry.ngay_san_xuat[:10],
                        'gio_luu_du_lieu': entry.gio_luu_du_lieu,
                        'tong_sl_sx': entry.tong_sl_sx,
                        'tong_sl_pp_kx': entry.tong_sl_pp_kx,
                        'tay_choi': entry.tay_choi,
                        'chau_dien': entry.chau_dien,
                        'buichi_chau': entry.buichi_chau,
                        'buichi_choi': entry.buichi_choi,
                        'pp_khac': entry.pp_khac} for entry in data]
    return JsonResponse(serialized_data, safe=False)


def add_category_lddk(request,id):
    data_id = category.objects.filter(date_id=id).order_by('-id').first()
    data_lddk = category_lddk.objects.get(date_1_id = id)
    slsx = data_id.tong_sl_sx
    slpp = data_id.tong_sl_pp_kx
    if request.method == 'POST':
        qc_choi = request.POST.get('qc_choi')
        ng_choi = request.POST.get('ng_choi')
        nham_choi = request.POST.get('nham_choi')

        qc_chau = request.POST.get('qc_chau')
        ng_chau = request.POST.get('ng_chau')
        nham_chau = request.POST.get('nham_chau')

        qc_bc_choi = request.POST.get('qc_bc_choi')
        ng_bc_choi = request.POST.get('ng_bc_choi')
        nham_bc_choi = request.POST.get('nham_bc_choi')

        qc_bc_chau = request.POST.get('qc_bc_chau')
        ng_bc_chau = request.POST.get('ng_bc_chau')
        nham_bc_chau = request.POST.get('nham_bc_chau')

        qc_pp_khac = request.POST.get('qc_pp_khac')
        ng_pp_khac = request.POST.get('ng_pp_khac')
        nham_pp_khac = request.POST.get('nham_pp_khac')

        tong_pp_qc = int(qc_choi) + int(qc_chau) + int(qc_bc_choi) + int(qc_bc_chau) + int(qc_pp_khac) 
        tong_pp_cong_doan = int(ng_choi) + int(ng_chau) + int(ng_bc_choi) + int(ng_bc_chau) + int(ng_pp_khac) 
        tong_pp_pdn = int(nham_choi) + int(nham_chau) + int(nham_bc_choi) + int(nham_bc_chau) + int(nham_pp_khac) 

        luu_xuat = request.POST.get('luu_xuat')
        luu_xuat_image = request.FILES.get('luu_xuat_image')
        note = request.POST.get('note')

        data_lddk.slsx = slsx
        data_lddk.slpp = slpp
        data_lddk.qc_choi = qc_choi
        data_lddk.ng_choi = ng_choi
        data_lddk.nham_choi = nham_choi
        data_lddk.qc_chau = qc_chau
        data_lddk.ng_chau = ng_chau
        data_lddk.nham_chau = nham_chau
        data_lddk.qc_bc_choi = qc_bc_choi
        data_lddk.ng_bc_choi = ng_bc_choi
        data_lddk.nham_bc_choi = nham_bc_choi
        data_lddk.qc_bc_chau = qc_bc_chau
        data_lddk.ng_bc_chau = ng_bc_chau
        data_lddk.nham_bc_chau = nham_bc_chau
        data_lddk.qc_pp_khac = qc_pp_khac
        data_lddk.ng_pp_khac = ng_pp_khac
        data_lddk.nham_pp_khac = nham_pp_khac
        data_lddk.tong_pp_qc = tong_pp_qc
        data_lddk.tong_pp_cong_doan = tong_pp_cong_doan
        data_lddk.tong_pp_pdn = tong_pp_pdn
        data_lddk.luu_xuat = luu_xuat
        data_lddk.luu_xuat_image = luu_xuat_image
        data_lddk.note = note
        data_lddk.save()

        return redirect('ccai0015_detail_data',id)

def search_date_lot(request):
    if request.method == 'GET':
        query = request.GET.get('query')  
        if query.strip() != '':
            search_date = x75.objects.filter(date_on_excel__icontains=query)
            result = []
            for date in search_date:
                result.append({'date': date.date_on_excel,'lot':date.lot,'id_date_url':f'/detail/ccai0015_detail_data/{date.id}/' }) 
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse([])
        
def delete_selected_records(request):
    if request.method == "POST" and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        selected_ids = request.POST.getlist("selectedIds[]")
        x75.objects.filter(id__in=selected_ids).delete()
        return JsonResponse({"message": "Selected records deleted successfully."})
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)
        
def generate_event_data(id):
    data = category.objects.filter(date_id=id).values()  # Lấy dữ liệu dưới dạng dictionary
    return data

def sse_update_data(request, id):
    def stream():
        last_updated = None
        while True:
            current_data = generate_event_data(id)
            if current_data != last_updated:
                yield f"data: {json.dumps(current_data)}\n\n"
                last_updated = current_data
                print(last_updated)
    response = StreamingHttpResponse(stream(), content_type='text/event-stream')
    response['Cache-Control'] = 'no-cache'
    return response
