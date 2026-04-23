from ziwei_const import *

FUNC_TIANGANHUA = '天干化'
FUNC_SHENGNIANHUA = '有生年'
FUNC_HAVESTAR = '有星'
PARA_JIEGONG = '借宫'
PARA_BENGONG = '本宫'

JIANKANG_PRE_RULE = [
    {
        "index": "A.1",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：10；较有可能因病手术或受伤，可能性分数：10",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "A.2",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_JIE}) and ({DIMENSION_BASIC}{PALACE_FUMU}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：10；较有可能因病手术或受伤，可能性分数：10",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "A.3",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：9；较有可能因病手术或受伤，可能性分数：9",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "A.4",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：8；较有可能因病手术或受伤，可能性分数：8",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "A.5",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUMU}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：8；较有可能因病手术或受伤，可能性分数：8",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "A.6",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：8；较有可能因病手术或受伤，可能性分数：8",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "B.1",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：9；较有可能因病手术或受伤，可能性分数：9",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "B.2",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_JIE}) and ({DIMENSION_BASIC}{PALACE_FUMU}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：9；较有可能因病手术或受伤，可能性分数：9",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "B.3",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：9；较有可能因病手术或受伤，可能性分数：9",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "B.4",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：8；较有可能因病手术或受伤，可能性分数：8",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "B.5",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：8；较有可能因病手术或受伤，可能性分数：8",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "B.6",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUMU}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，有可能发生重大生理或心理疾病，可能性分数：8；较有可能因病手术或受伤，可能性分数：8",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.1",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.2",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.3",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.4",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_MING})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.5",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_MING})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.6",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.7",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年有一定机率在特定年份发生较重疾病或精神巨大压力，可能性分数：6。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.8",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_QIANYI})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.9",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_MING}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_MING})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.10",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_JIE})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.11",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_JIE})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.12",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_JIE}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.13",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_JIE}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：6；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.14",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_FUMU}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUMU})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.15",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_JIE})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.16",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUDE})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.17",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUDE})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.18",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.19",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年有一定机率在特定年份发生较重疾病或精神巨大压力，可能性分数：6。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.20",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_CAIBO})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "C.21",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUDE})",
        "result": "这十年应特别注意身心健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.1",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.2",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.3",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.4",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8。",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.5",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.6",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.7",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "这十年应注意在特定年份发生较重疾病或精神巨大压力，可能性分数：6；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.8",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_QIANYI}宫)",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.9",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_MING}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.10",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUMU}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.11",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.12",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUMU}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_FUMU}宫)",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.13",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_JIE}宫)",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.14",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUMU}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.15",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.16",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_FUDE}宫)",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.17",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUDE}宫)",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.18",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "D.19",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_CAIBO}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_CAIBO}宫)",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.1",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.2",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.3",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.4",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；较有可能因病手术或受伤，可能性分数：8；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.5",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.6",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.7",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.8",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_QIANYI})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.9",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_MING}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.10",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_JIE})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.11",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_JIE})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.12",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_JIE}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.14",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_FUMU}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUMU})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.15",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_JIE})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.16",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUDE})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.17",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUDE})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.18",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.19",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.20",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_CAIBO}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_CAIBO})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "E.21",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_CAIBO}) and ({DIMENSION_BASIC}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUDE})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.1",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.2",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.3",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.4",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：8；较有可能因病手术或受伤，可能性分数：8；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.5",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.6",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.7",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5； ",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.8",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_QIANYI}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_QIANYI})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.9",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_MING}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_MING})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.10",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.11",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.12",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_CAIBO}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_CAIBO})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.13",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_FUDE})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.14",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_CAIBO}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.15",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_CAIBO}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_SHENGNIANHUA}{HUA_JI})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：5；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.16",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_JIE})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.17",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_JIE})",
        "result": "十年中特定年份需注意疾病或较大的精神压力，可能性分数：6；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.18",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUMU}{FUNC_SHENGNIANHUA}{HUA_QUAN})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "F.19",
        "rule": f"({DIMENSION_RANGE}{PALACE_FUDE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_RANGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_FUMU}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_RANGE}{PALACE_FUMU})",
        "result": "这十年应特别注意身体健康问题，在特定年份有较大机率发生较严重疾病或精神创伤，可能性分数：7；",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    }
]

JIANKANG_LOC_RULE = [
    {
        "index": "发病年份.1",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_AGE}{PALACE_QIANYI})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：10；健康基础差者有可能手术",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "发病年份.2",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_AGE}{PALACE_FUMU})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：10；健康基础差者有可能手术",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "发病年份.3",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_AGE}{PALACE_QIANYI}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_AGE}{PALACE_MING})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：10；较有可能因病手术或受伤，定位准确性分数：10；",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "发病年份.4",
        "rule": f"({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_AGE}{PALACE_FUMU}) and ({DIMENSION_RANGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_AGE}{PALACE_JIE})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：10；较有可能因病手术或受伤，定位准确性分数：10；",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "发病年份.5",
        "rule": f"({DIMENSION_AGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：9；",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "发病年份.6",
        "rule": f"({DIMENSION_AGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：9；",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "发病年份.7",
        "rule": f"({DIMENSION_AGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_QIANYI}) and ({DIMENSION_BASIC}{PALACE_QIANYI}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_QIANYI})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：9；较有可能因病手术或受伤，定位准确性分数：8；",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "发病年份.8",
        "rule": f"({DIMENSION_AGE}{PALACE_JIE}{FUNC_TIANGANHUA}{HUA_JI}{DIMENSION_BASIC}{PALACE_FUMU}) and ({DIMENSION_BASIC}{PALACE_FUMU}{FUNC_TIANGANHUA}{HUA_QUAN}{DIMENSION_BASIC}{PALACE_FUMU})",
        "result": "这年很可能身体出现较严重健康问题或严重的精神压力，定位准确性分数：9；较有可能因病手术或受伤，定位准确性分数：8；",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    },
    {
        "index": "手术判定.1",
        "rule": f"({DIMENSION_AGE}{PALACE_JIE}{PARA_JIEGONG}{FUNC_HAVESTAR}{MINOR_QINGYANG}) or ({DIMENSION_AGE}{PALACE_JIE}{PARA_JIEGONG}{FUNC_HAVESTAR}{ADJECTIVE_TIANXING})",
        "result": "很大可能会做手术",
        "premise": "前置条件中同事项的可能性分数达到7分以上（当存在多个前置条件时，同事项的可能性分数相加作为最终的可能性分数）",
        "solution": "建议每年固定查体，及早发现，及早治疗。",
        "reason": "基于本命盘，大限盘。流年盘。以及命盘盘中疾厄相关参数。使用四化、飞星技法 。结合星耀强弱。综合判定得出"
    }
]