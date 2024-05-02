from django.shortcuts import render
from server.models import server_test
from Tam_Sat_M100_A75.models import TAM_SAT_A75_M100,category
from django.http import JsonResponse

def detail_date(request,id):
    date = TAM_SAT_A75_M100.objects.filter(client_id = id).order_by('-id')[:10]
    name_space_id = server_test.objects.get(id=id)
    name_space = name_space_id.name_client
    context = {'date': date,'name_space':name_space}
    return render(request, 'static/TAM_SAT_A75_M100/index_date.html', context)

def chart_date(request, id):
    date = TAM_SAT_A75_M100.objects.filter(client_id=id).order_by('-id')[:10]
    dat_and_last_records = []
    for dat in date:
        last_category_record = dat.category_set.order_by('id').last()
        if last_category_record:
            tong_so_luong_pp = int(last_category_record.tong_so_luong_pp_cam_1) + int(last_category_record.tong_so_luong_pp_cam_2) 
            last_record_data = {
                'tong_so_luong_sx': last_category_record.tong_so_luong_sx,
                'tong_so_luong_pp': tong_so_luong_pp ,
            }
        else:
            last_record_data = None
        dat_and_last_records.append({'date_on_excel': dat.date_on_excel,'lot': dat.lot, 'last_record': last_record_data,})
    return JsonResponse({'dat_and_last_records': dat_and_last_records})

def detail_data(request,id):
    data = category.objects.filter(date_id = id)
    context = {'data': data, 'name_space':'ccai0004','date_id': id}
    return render(request, 'static/TAM_SAT_A75_M100/index_data_realtime.html', context)

def detail_data_realtime(request, id):
    data = category.objects.filter(date_id=id)
    serialized_data = [{'date_id': entry.date_id,
                        'ngay_san_xuat': entry.ngay_san_xuat[:10],
                        'gio_luu_du_lieu': entry.gio_luu_du_lieu,

                        'tong_so_luong_sx': entry.tong_so_luong_sx,

                        'keo_dinh_truc_cam_1': entry.keo_dinh_truc_cam_1,
                        'keo_dinh_ban_comi_cam_1': entry.keo_dinh_ban_comi_cam_1,
                        'keo_it_keo_khong_deu_cam_1': entry.keo_it_keo_khong_deu_cam_1,
                        'keo_bi_thung_lo_cam_1': entry.keo_bi_thung_lo_cam_1,
                        'phe_pham_khac_cam_1': entry.phe_pham_khac_cam_1,
                        'tong_so_luong_pp_cam_1': entry.tong_so_luong_pp_cam_1,

                        'keo_dinh_truc_cam_2': entry.keo_dinh_truc_cam_2,
                        'keo_dinh_ban_comi_cam_2': entry.keo_dinh_ban_comi_cam_2,
                        'keo_it_keo_khong_deu_cam_2': entry.keo_it_keo_khong_deu_cam_2,
                        'keo_bi_thung_lo_cam_2': entry.keo_dinh_truc_cam_2,
                        'phe_pham_khac_cam_2': entry.keo_it_keo_khong_deu_cam_2,
                        'tong_so_luong_pp_cam_2': entry.tong_so_luong_pp_cam_2
                        
                        } for entry in data]
    return JsonResponse(serialized_data, safe=False)

def chart_data_realtime(request, id):
    last_entry = category.objects.filter(date_id=id).order_by('-id').first()
    last_entry_data = {
                        'date_id': last_entry.date_id,
                        'ngay_san_xuat': last_entry.ngay_san_xuat[:10],
                        'gio_luu_du_lieu': last_entry.gio_luu_du_lieu,

                        'tong_so_luong_sx': last_entry.tong_so_luong_sx,

                        'keo_dinh_truc_cam_1': last_entry.keo_dinh_truc_cam_1,
                        'keo_dinh_ban_comi_cam_1': last_entry.keo_dinh_ban_comi_cam_1,
                        'keo_it_keo_khong_deu_cam_1': last_entry.keo_it_keo_khong_deu_cam_1,
                        'keo_bi_thung_lo_cam_1': last_entry.keo_bi_thung_lo_cam_1,
                        'phe_pham_khac_cam_1': last_entry.phe_pham_khac_cam_1,
                        'tong_so_luong_pp_cam_1': last_entry.tong_so_luong_pp_cam_1,

                        'keo_dinh_truc_cam_2': last_entry.keo_dinh_truc_cam_2,
                        'keo_dinh_ban_comi_cam_2': last_entry.keo_dinh_ban_comi_cam_2,
                        'keo_it_keo_khong_deu_cam_2': last_entry.keo_it_keo_khong_deu_cam_2,
                        'keo_bi_thung_lo_cam_2': last_entry.keo_dinh_truc_cam_2,
                        'phe_pham_khac_cam_2': last_entry.keo_it_keo_khong_deu_cam_2,
                        'tong_so_luong_pp_cam_2': last_entry.tong_so_luong_pp_cam_2
                        }
    
    print(last_entry_data)
    return JsonResponse(last_entry_data, safe=False)

def search_date_lot(request):
    if request.method == 'GET':
        query = request.GET.get('query')  
        if query.strip() != '':
            search_date = TAM_SAT_A75_M100.objects.filter(date_on_excel__icontains=query)
            result = []
            for date in search_date:
                result.append({'date': date.date_on_excel,'lot':date.lot,'id_date_url':f'/detail/ccai0004_detail_data/{date.id}/' }) 
            return JsonResponse(result, safe=False)
        else:
            return JsonResponse([])
        
def delete_selected_records(request):
    if request.method == "POST" and request.META.get("HTTP_X_REQUESTED_WITH") == "XMLHttpRequest":
        selected_ids = request.POST.getlist("selectedIds[]")
        TAM_SAT_A75_M100.objects.filter(id__in=selected_ids).delete()
        return JsonResponse({"message": "Selected records deleted successfully."})
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)
    
# def Category_lddk(request,id):
#     data_id = category.objects.filter(date_id=id).order_by('-id').first()
#     data_lddk = category_lddk.objects.get(date_1_id = id)
#     slsx = data_id.tong_sl_sx
#     slpp = data_id.tong_sl_pp_kx
#     if request.method == 'POST':
#         qc_choi = request.POST.get('qc_choi')
#         ng_choi = request.POST.get('ng_choi')
#         nham_choi = request.POST.get('nham_choi')

#         qc_chau = request.POST.get('qc_chau')
#         ng_chau = request.POST.get('ng_chau')
#         nham_chau = request.POST.get('nham_chau')

#         qc_bc_choi = request.POST.get('qc_bc_choi')
#         ng_bc_choi = request.POST.get('ng_bc_choi')
#         nham_bc_choi = request.POST.get('nham_bc_choi')

#         qc_bc_chau = request.POST.get('qc_bc_chau')
#         ng_bc_chau = request.POST.get('ng_bc_chau')
#         nham_bc_chau = request.POST.get('nham_bc_chau')

#         qc_pp_khac = request.POST.get('qc_pp_khac')
#         ng_pp_khac = request.POST.get('ng_pp_khac')
#         nham_pp_khac = request.POST.get('nham_pp_khac')

#         tong_pp_qc = int(qc_choi) + int(qc_chau) + int(qc_bc_choi) + int(qc_bc_chau) + int(qc_pp_khac) 
#         tong_pp_cong_doan = int(ng_choi) + int(ng_chau) + int(ng_bc_choi) + int(ng_bc_chau) + int(ng_pp_khac) 
#         tong_pp_pdn = int(nham_choi) + int(nham_chau) + int(nham_bc_choi) + int(nham_bc_chau) + int(nham_pp_khac) 

#         luu_xuat = request.POST.get('luu_xuat')
#         luu_xuat_image = request.FILES.get('luu_xuat_image')
#         note = request.POST.get('note')

#         data_lddk.slsx = slsx
#         data_lddk.slpp = slpp
#         data_lddk.qc_choi = qc_choi
#         data_lddk.ng_choi = ng_choi
#         data_lddk.nham_choi = nham_choi
#         data_lddk.qc_chau = qc_chau
#         data_lddk.ng_chau = ng_chau
#         data_lddk.nham_chau = nham_chau
#         data_lddk.qc_bc_choi = qc_bc_choi
#         data_lddk.ng_bc_choi = ng_bc_choi
#         data_lddk.nham_bc_choi = nham_bc_choi
#         data_lddk.qc_bc_chau = qc_bc_chau
#         data_lddk.ng_bc_chau = ng_bc_chau
#         data_lddk.nham_bc_chau = nham_bc_chau
#         data_lddk.qc_pp_khac = qc_pp_khac
#         data_lddk.ng_pp_khac = ng_pp_khac
#         data_lddk.nham_pp_khac = nham_pp_khac
#         data_lddk.tong_pp_qc = tong_pp_qc
#         data_lddk.tong_pp_cong_doan = tong_pp_cong_doan
#         data_lddk.tong_pp_pdn = tong_pp_pdn
#         data_lddk.luu_xuat = luu_xuat
#         data_lddk.luu_xuat_image = luu_xuat_image
#         data_lddk.note = note
#         data_lddk.save()

#         return redirect('ccai0015_detail_data',id)



