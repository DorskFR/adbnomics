import asyncio
from adbnomics import ConcurAsyncGen, Cleaner, Saver

SAMPLE = [
    {"AFRREO": "All_Indicators"},
    {"AFRREO": "BCA_BP6_GDP_PT"},
    {"AFRREO": "BFD_BP6_GDP_PT"},
    {"AFRREO": "BG_BP6_GDP_PT"},
    {"AFRREO": "BMGS_BP6_GDP_PT"},
    {"AFRREO": "BXGS_BP6_GDP_PT"},
    {"AFRREO": "D_G_GDP_PT"},
    {"AFRREO": "ENEER_IX"},
    {"AFRREO": "EREER_IX"},
    {"AFRREO": "FDSAOP_GDP_PT"},
    {"AFRREO": "FDSAOP_PC_PP_PT"},
    {"AFRREO": "FMB_GDP_PT"},
    {"AFRREO": "FMB_PC_PP_PT"},
    {"AFRREO": "GGR_G01_GDP_PT"},
    {"AFRREO": "GGXCNLXG_G01_GDP_PT"},
    {"AFRREO": "GGXCNL_G01_GDP_PT"},
    {"AFRREO": "GGXWDG_G01_GDP_PT"},
    {"AFRREO": "GGX_G01_GDP_PT"},
    {"AFRREO": "IAR_BP6_MI_MH"},
    {"AFRREO": "NGDPRPC_PC_PP_PT"},
    {"AFRREO": "NGDPXO_R_PC_PP_PT"},
    {"AFRREO": "NGDP_R_PC_PP_PT"},
    {"AFRREO": "NGS_GDP_PT"},
    {"AFRREO": "NI_GDP_PT"},
    {"AFRREO": "PCPI_EOP_PC_PP_PT"},
    {"AFRREO": "PCPI_PC_PP_PT"},
    {"AFRREO": "TTT_IX"},
    {"APDREO": "All_Indicators"},
    {"APDREO": "BCA_GDP_BP6"},
    {"APDREO": "GGXCNL_GDP"},
    {"APDREO": "LUR"},
    {"APDREO": "NGDP_RPCH"},
    {"APDREO": "NGDP_R_PPP_PC_PCH"},
    {"APDREO": "PCPIE_PCH"},
    {"APDREO": "PCPI_PCH"},
    {"BOP": "BACK_BP6_EUR"},
    {"BOP": "BACK_BP6_USD"},
    {"BOP": "BACK_BP6_XDC"},
    {"BOP": "BAXEF_BP6_EUR"},
    {"BOP": "BAXEF_BP6_USD"},
    {"BOP": "BAXEF_BP6_XDC"},
    {"BOP": "BCAXF_BP6_EUR"},
    {"BOP": "BCAXF_BP6_USD"},
    {"BOP": "BCAXF_BP6_XDC"},
    {"BOP": "BCA_BP6_EUR"},
    {"BOP": "BCA_BP6_USD"},
    {"BOP": "BCA_BP6_XDC"},
    {"BOP": "BEFDDAAI_BP6_EUR"},
    {"BOP": "BEFDDAAI_BP6_USD"},
    {"BOP": "BEFDDAAI_BP6_XDC"},
    {"BOP": "BEFDDAAPI_BP6_EUR"},
    {"BOP": "BEFDDAAPI_BP6_USD"},
    {"BOP": "BEFDDAAPI_BP6_XDC"},
    {"BOP": "BEFDDAAP_BP6_EUR"},
    {"BOP": "BEFDDAAP_BP6_USD"},
    {"BOP": "BEFDDAAP_BP6_XDC"},
    {"BOP": "BEFDDAA_BP6_EUR"},
    {"BOP": "BEFDDAA_BP6_USD"},
    {"BOP": "BEFDDAA_BP6_XDC"},
    {"BOP": "BEFDDCAI_BP6_EUR"},
    {"BOP": "BEFDDCAI_BP6_USD"},
    {"BOP": "BEFDDCAI_BP6_XDC"},
    {"BOP": "BEFDDCAP_BP6_EUR"},
    {"BOP": "BEFDDCAP_BP6_USD"},
    {"BOP": "BEFDDCAP_BP6_XDC"},
    {"BOP": "BEFDDCA_BP6_EUR"},
    {"BOP": "BEFDDCA_BP6_USD"},
    {"BOP": "BEFDDCA_BP6_XDC"},
    {"BOP": "BEFDDRAI_BP6_EUR"},
    {"BOP": "BEFDDRAI_BP6_USD"},
    {"BOP": "BEFDDRAI_BP6_XDC"},
    {"BOP": "BEFDDRAP_BP6_EUR"},
    {"BOP": "BEFDDRAP_BP6_USD"},
    {"BOP": "BEFDDRAP_BP6_XDC"},
    {"BOP": "BEFDDRA_BP6_EUR"},
    {"BOP": "BEFDDRA_BP6_USD"},
    {"BOP": "BEFDDRA_BP6_XDC"},
    {"BOP": "BEFDDRPI_BP6_EUR"},
    {"BOP": "BEFDDRPI_BP6_USD"},
    {"BOP": "BEFDDRPI_BP6_XDC"},
    {"BOP": "BEFDDRPP_BP6_EUR"},
    {"BOP": "BEFDDRPP_BP6_USD"},
    {"BOP": "BEFDDRPP_BP6_XDC"},
    {"BOP": "BEFDDRP_BP6_EUR"},
    {"BOP": "BEFDDRP_BP6_USD"},
    {"BOP": "BEFDDRP_BP6_XDC"},
    {"BOP": "BEFDDSAI_BP6_EUR"},
    {"BOP": "BEFDDSAI_BP6_USD"},
    {"BOP": "BEFDDSAI_BP6_XDC"},
    {"BOP": "BEFDDSAP_BP6_EUR"},
    {"BOP": "BEFDDSAP_BP6_USD"},
    {"BOP": "BEFDDSAP_BP6_XDC"},
    {"BOP": "BEFDDSA_BP6_EUR"},
    {"BOP": "BEFDDSA_BP6_USD"},
    {"BOP": "BEFDDSA_BP6_XDC"},
    {"BOP": "BEFDD_BP6_EUR"},
    {"BOP": "BEFDD_BP6_USD"},
    {"BOP": "BEFDD_BP6_XDC"},
    {"BOP": "BEFDE_BP6_EUR"},
    {"BOP": "BEFDE_BP6_USD"},
    {"BOP": "BEFDE_BP6_XDC"},
    {"BOP": "BEFD_BP6_EUR"},
    {"BOP": "BEFD_BP6_USD"},
    {"BOP": "BEFD_BP6_XDC"},
    {"BOP": "BEFISGIMF_BP6_EUR"},
    {"BOP": "BEFISGIMF_BP6_USD"},
    {"BOP": "BEFISGIMF_BP6_XDC"},
    {"BOP": "BEFISIG_BP6_EUR"},
    {"BOP": "BEFISIG_BP6_USD"},
    {"BOP": "BEFISIG_BP6_XDC"},
    {"BOP": "BEFIS_BP6_EUR"},
    {"BOP": "BEFIS_BP6_USD"},
    {"BOP": "BEFIS_BP6_XDC"},
    {"BOP": "BEFOE_BP6_EUR"},
    {"BOP": "BEFOE_BP6_USD"},
    {"BOP": "BEFOE_BP6_XDC"},
    {"BOP": "BEFOODCBAAI_BP6_EUR"},
    {"BOP": "BEFOODCBAAI_BP6_USD"},
    {"BOP": "BEFOODCBAAI_BP6_XDC"},
    {"BOP": "BEFOODCBAAPI_BP6_EUR"},
    {"BOP": "BEFOODCBAAPI_BP6_USD"},
    {"BOP": "BEFOODCBAAPI_BP6_XDC"},
    {"BOP": "BEFOODCBAAP_BP6_EUR"},
    {"BOP": "BEFOODCBAAP_BP6_USD"},
    {"BOP": "BEFOODCBAAP_BP6_XDC"},
    {"BOP": "BEFOODCBAA_BP6_EUR"},
    {"BOP": "BEFOODCBAA_BP6_USD"},
    {"BOP": "BEFOODCBAA_BP6_XDC"},
    {"BOP": "BEFOODCBCAI_BP6_EUR"},
    {"BOP": "BEFOODCBCAI_BP6_USD"},
    {"BOP": "BEFOODCBCAI_BP6_XDC"},
    {"BOP": "BEFOODCBCAP_BP6_EUR"},
    {"BOP": "BEFOODCBCAP_BP6_USD"},
    {"BOP": "BEFOODCBCAP_BP6_XDC"},
    {"BOP": "BEFOODCBCA_BP6_EUR"},
    {"BOP": "BEFOODCBCA_BP6_USD"},
    {"BOP": "BEFOODCBCA_BP6_XDC"},
    {"BOP": "BEFOODCBND_BP6_EUR"},
    {"BOP": "BEFOODCBND_BP6_USD"},
    {"BOP": "BEFOODCBND_BP6_XDC"},
    {"BOP": "BEFOODCBPP_BP6_EUR"},
    {"BOP": "BEFOODCBPP_BP6_USD"},
    {"BOP": "BEFOODCBPP_BP6_XDC"},
    {"BOP": "BEFOODCBRAI_BP6_EUR"},
    {"BOP": "BEFOODCBRAI_BP6_USD"},
    {"BOP": "BEFOODCBRAI_BP6_XDC"},
    {"BOP": "BEFOODCBRAP_BP6_EUR"},
    {"BOP": "BEFOODCBRAP_BP6_USD"},
]


def make_url(provider, dataset, indicator):
    base_url = "https://api.db.nomics.world/v22/series/"
    params = "?observations=true&metadata=false&format=json&limit=1000&offset=0"
    return f"{base_url}{provider}/{dataset}/A..{indicator}{params}"


def make_urls():
    urls = [make_url("IMF", k, v) for row in SAMPLE for k, v in row.items()]
    return urls


async def process_result(result):
    if result.get("message") and "not found" in result.get("message"):
        return
    cleaner = Cleaner(result)
    saver = Saver(cleaner.result)
    saver.to_csv(folder="output")


async def main():
    asyncgen = ConcurAsyncGen()
    urls = make_urls()
    concurrency = 60
    generator = asyncgen.as_completed_with_concurrency(concurrency, *urls)
    async for result in generator:
        await process_result(result)


if __name__ == "__main__":
    asyncio.run(main())


# async def download_toc():
#     response_json = await asyncgen.get_async(url)


# toc
# while True:
# fetch list of datasets
# append(result)
# if found > limit + offset
# offset += limit
# iterate over toc and build list of URLS
