from extractors.indeed import extract_ind_jobs

keyword = input("검색 키워드를 입력해주세요.")


results = extract_ind_jobs(keyword)

file = open(f"{keyword}.csv", "w", encoding="utf-8")
file.write("회사 이름, 위치, 정보, 공고 업로드 시간, 링크\n")

for result in results:
    file.write(
        f"{result['company_name']},{result['location']},{result['detail_info']},{result['create_at']},{result['link']}\n"
    )

file.close()
