from Cryptodome.PublicKey import RSA
from Cryptodome.Util.number import bytes_to_long


class SlaKey:
    vendor = None
    da_codes = None
    name = None
    d = None
    n = None
    e = None

    def __init__(self, vendor, da_codes, name, d, n, e):
        self.vendor = vendor
        self.da_codes = da_codes
        self.name = name
        self.d = d
        self.n = n
        self.e = e
        if isinstance(d,int):
            d_da = d
        else:
            d_da = bytes_to_long(bytes.fromhex(self.d))
        if isinstance(n, int):
            n_da = n
        else:
            n_da = bytes_to_long(bytes.fromhex(self.n))
        if isinstance(e, int):
            e_da = e
        else:
            e_da = bytes_to_long(bytes.fromhex(self.e))
        self.key = RSA.construct((n_da,d_da,e_da))


da_sla_keys = [
    # lk/files/pbp/keys/toolauth/da_prvk.pem
    SlaKey(vendor="KaiOS",
           da_codes=[],
           name="",
           d="928d2a63d56bc42c3c02e836c025f6db39f06d57480dc705f3eaf238120a2b0d8fc00ec3cdf209615ca41bf73ae499dd9accb09b99fbb4046087008aab48d96f437292c160092dfc4ae33f94acee374e584b9d70d90ca46664d31cf72bba302e6eafab68e13a7f1ed9fa0ddc2604f3164bc97bc8c1b0be9db1d76d1d970ea36f4af8ad2ce0ab5b7ca6b4f99c133fa3f8ff9c92da874394d0e8f1bdbb83c8e811a344a5b5a7251c9b4fb4ad0ac494a2c50a1a79fa9b3992d749535b691dc2f016cee493e41cd2033190c4c0497f689e48bae5d3ad28cb0e8d17dae7f4e8c034ab60ab330f678fbfdd2c9716bfa6a617339d248b46df1593d5317b3af44a864641",
           n="9BB734774443D77557A76E24B10733787750D90D09C869CD606D54F28978EA6220DC9948B3C9E89284F8551D6166F3754B6A3B890AC9CDA9E37DFAA0C1317E351CE5107C4273795949C6CCE638314AB1A345385D7642CB8D055A1F410C7D7E24A6F0A2AAB8184E773D21B3754A947541680F2C1A8D6BA5BEFD3B6E1FC28EC0B61D55B1454383F2C3E8BD27170A25978608F6788B90A2FC34F0CE35056BF7520795C8C60232CBBC0B0399367AF937869CA45CF737A8A066127893E93166C433298DD6FD009E6790E743B3392ACA8EA99F61DFC77BD99416DDA4B8A9D7E4DA24217427F3584119A4932016F1735CC63B12650FDDDA73C8FCFBC79E058F36219D3D",
           e="010001"),
    # lk/files/pbp/keys/toolauth/da_prvk.pem
    SlaKey(vendor="Rowan",
           da_codes=[],
           name="",
           d="09976537029b4362591c5b13873f223de5525d55df52dde283e52afa67f6c9dbf1408d2fb586a624efc93426f5f3be981f80e861ddd975a1e5e662db84f5164804a3ae717605d7f15866df9ed1497c38fdd6197243163ef22f958d7b822c57317203e9a1e7d18dad01f15054facdbddb9261a1272638da661fe4f9f0714ecf00e6541cc435afb1fd75a27d34b17ad400e9474ba850dafce266799caff32a058ff71e4c2daacaf8ba709e9ca4dc87584a7ffe8aa9a0a160ed069c3970b7dae3987ded71bd0bc824356987bd74363d46682c71913c3edbdb2a911f701f23aee3f8dd98180b5a138fd5ad74743682d2d2d1bb3d92786710248f316dd8391178ea81",
           n="D16403466C530EF9BB53C1E8A96A61A4E332E17DC0F55BB46D207AC305BAE9354EAAC2CB3077B33740D275036B822DB268200DE17DA3DB7266B27686B8970B85737050F084F8D576904E74CD6C53B31F0BB0CD60686BF67C60DA0EC20F563EEA715CEBDBF76D1C5C10E982AB2955D833DE553C9CDAFD7EA2388C02823CFE7DD9AC83FA2A8EB0685ABDAB56A92DF1A7805E8AC0BD10C0F3DCB1770A9E6BBC3418C5F84A48B7CB2316B2C8F64972F391B116A58C9395A9CE9E743569A367086D7771D39FEC8EBBBA3DD2B519785A76A9F589D36D637AF884543FD65BAC75BE823C0C50AA16D58187B97223625C54C66B5A5E4DBAEAB7BE89A4E340A2E241B09B2F",
           e="010001"),
    """
    SlaKey(vendor="Generic",
           da_codes=[],
           name="VERIFIED_BOOT_IMG_AUTH_KEY.ini",
           d=0xDACD8B5FDA8A766FB7BCAA43F0B16915CE7B47714F1395FDEBCF12A2D41155B0FB587A51FECCCB4DDA1C8E5EB9EB69B86DAF2C620F6C2735215A5F22C0B6CE377AA0D07EB38ED340B5629FC2890494B078A63D6D07FDEACDBE3E7F27FDE4B143F49DB4971437E6D00D9E18B56F02DABEB0000B6E79516D0C8074B5A42569FD0D9196655D2A4030D42DFE05E9F64883E6D5F79A5BFA3E7014C9A62853DC1F21D5D626F4D0846DB16452187DD776E8886B48C210C9E208059E7CAFC997FD2CA210775C1A5D9AA261252FB975268D970C62733871D57814098A453DF92BC6CA19025CD9D430F02EE46F80DE6C63EA802BEF90673AAC4C6667F2883FB4501FA77455,
           n=0x8BC9B1F7A559BCDD1717F3F7BFF8B858743892A6338D21D0BE2CE78D1BCB8F61A8D31822F694C476929897E4B10753DDBE45A2276C0EFEE594CF75E47016DA9CDB3D8EB6C3E4C5D69B8BCCE1AE443CF299C22B905300C85875E8DBB8231F4E9949D8CF9D8E0F40E93F29F843420F22CD9D080A45A4407F58F3609D03A7DB950D3D847B8B4E7D50DB6359D37A2DD730D3CE77F8FB2A33C095B0A6CF3E08593E4F70254DCDF671790F530EC07C3CD1E80199CB42F24ACA92DB5996F2119003F502E16D88EB4E4A8DEAE4036558D2A52F5C9960B0FBBC6F6FA75EFF6F5A173CE1A82539A35973D568B8918ED12F7610748BEB0239A5006257E19574C77F4133A269,
           e="010001"),
    """,
    SlaKey(vendor="Generic",
           da_codes=[],
           name="CodeSigKey",
           d="00D57BCF5934CE1A035F4598B42DAD4BC8AE7577FB6D81FA232317E8EE7C4FBB33772EFE378DF7DFE5369BB9ACAB1008FA1CFBA737890012A883B372B15932335B689B46A32F1B383B75F0DE2E1B5B0B9F4E1C3E780C2AB0CD3671EB4E34F30BB4C630A60D168CA124810D0F91A1ACC8EFDCEE52D4762BB35813BCC93878E1D15B750561B78006B4C13A8F76B5F10C941E5776C21192357A9B9D7E02C0FC812D2B154671863DE97CE3ED07F90624A0CADD04079E145168A3558A64786820192F5B638354DA69520288B976296961C337FB18A90120F2B6B365C0E1A57CE4119AE8BC718E08FDA33F1F42AA1C91AED090EC6B5656A66C246F89FDE5FD41A76671",
           n="01C6B6A1DDF05E818E3DFE16101C5DF65939F352EAB8AACA91CB5BFEC15A1989DD7553343683BC30BB38E45F15BF17BCCAB16A41D695A4318F26504675FE83E92EE21C991C0FBA705395B4A34C331842D8A6F69846B58CC67306E3DE27B05666A6C4372E3FC0D92F314805EDD5B1CB7D25BF3CF9CA9C33C36D97B0B37DA8A44A7A1CA651679D8D680557740C7C1CA25D84BDD12136C2930432808F28265D1E33E667389E4806D865F3CC06329534F7A11861EB688545DCCCEF0B04E96735A08368FA31A1F3260073B31299B216192E620B8D1EA468925ADBD627C49EFC3623658F3CF8AD6D8556272E48FA7711E650287DA19196610F036B6C0D394E42C121D1",
           e="010001"),
    SlaKey(vendor="Generic",
           da_codes=[],
           name="SecureROSigKey",
           d="040AB412E994921780E7D3AC4E665B5018BAD2221D93A236FCD3D4245BB14EF5E715B687254BFC5D5C058FF5C33AF644E6B03748A6ABFDFAFF808265B9C12B42C2164826B3A8CD5D6B3295E025618AED68D33E02D75FB8C69FDE6753AF454EAA92F448961C5D11DFD8D2D5125E54C71DE5792EAD4B4AD2A47ED2F144C664A2EC2B5C527D4C4570162EBADF6FA6AA19D86C927257BDA4AC4B471AD94AC16C8A97E9201101EF268E35E66835FE9831F3D18495BA15B3FCD9089B4569F770896674173647EFED86F4570CE6118E48A7EDD6CE2A2ED72A2E6FD615A323708F0881443B6C6DEF3800B392385E060AAC6CE086DDBA9227027F80B0DFDF691A1ED8A601",
           n="041EDF18B2702830A0D1D6D2C0C9833C46D55636929ABC8CBF62D03A8E352697F536DDF250E6CA5F1153A9227FEA4F6C4A91CF118FD821ABA9020FFC6AA05D4C361177AA384ACEE201E1326D5A0E1D566E74DA51CD735841FB5638E03F4E9A5AC58D0123F8E057686541E424F83508D1CEADDE7A893F57B852ECFF27953F53030953859EA265C0C7155F6B730E902BC23FEB58077E8D439606B164635D5AA0C53657BF2143EEE86F06781573BED22DD3E792591A263F2357CC42AEF4B8DB585987A311A022C4442A4DFA1C4891D8ADA1B231A92096E16D9C718FB09DFC0A5B008BB8243BF32C537A6B19542E37311085197B6BE8DA54EE1D6BC28BA94E0079CB",
           e="010001"),
]

brom_sla_keys = [
    SlaKey(vendor="Generic",
           da_codes=[],
           name="IMG_AUTH_KEY.ini",
           d="4BD992E9A2230CD2ABEF49E4F6A7E11D7E2ADD24847787B320239829C560D5EAB94B8304317C938E9358E94758AE60D9B13F2913DD1A749A9941FACAFAB574D70EBBFBCC0133A4BE2134CBA3CE7EE18A6D3CC98D33DAB06AEEE512F405A3248EA316ABC31A2758D4C5A7B9DFCC02C2508A492EF3760A0D4CDA827CFFCADD11ED",
           n="5FFF0B70D5DE3FC5BF41CB824B4BFD14820571CE57EDD3E7C668CC570E718DB07DCC7A6CACD0E80DADC38AA33DB37816839D97980DF3E577A6E0B1169D708071E17DD259CFE538DBDA804A2FC07D795841F2F59DEE023A9919360D0A3F4647FDF5657D9FC5944C8BFA2802336BA23AFDCDE8D546E8806EB532AA7F95A01D8DD1",
           e="010001"),
    """SlaKey(vendor="Generic",
           da_codes=[],
           name="AuthGen_SV5.ini",
           d="9a3c3d4da0650cef38ed96ef833904c9c13835199367c7b9cb03a55e7aa482016a820dfe597cd54dd1f81fd879cf070ec0c25899ac5a49822db09675a92acf6a01e0f8f538bbe66de48ca9bdca313b616470d9ec2914356d03c95f7d9236549e5a21457e4dd5fcaf09046c47ca7436f06cd7b82cb6d2a936fca88b707f6ce28f33110fea1ec363e8482419db901cb0d38e574fe0c02ad117166b40ec78f59aaa7f3eafa425010a95614e046651273a6cb1371380c4e6ce81bdb892db6ff4892cc4d8c613a8fb3fec1e72c279052896872fc23da07fba63783374f3be8e16a15e0a04a139108dd6ac239f191135f4a895e27c670de065d2248e3f9c7e920fd001",
           n="008C8BF38EB2FC7FC06D567DBF70E9C34BE4281C4239ED9C58A6B598C3AE7821815D94D0B463463EEBBD69FF6AF990AE0499B6C3B3CADCD91D54499CD66E5314DB610FC0C6CAEEB1F16B6F2D451E3F2B2D515008917FCEC50ADA4CE0699BCF247D5AE2A1DDD34C48624A657CCB11CE5F8C6CE92CAB6038EFC2A89E42E029488C02C3CF21947C86D51BBA8EF540A2A7CE85356F431891261D860B518E89DD73B2D240461ACB66BCC213403145DE83F6963147E65274EA1E45DB2D231E0774ECC86E4F2328F8A90835C4FDEF1088DDBA1D8F7CA0CA732A64BDA6816162C0F88F02CF97634D85530968CBF8B7CE6A8B67D53BBFB4910843EA413135D56FB5074445",
           e="010001"),
    """,
    SlaKey(vendor="Generic",
           da_codes=[],
           name="ROWAN / 0_2048_key.pem / CHIP_TEST_KEY.ini / lk/files/pbp/keys/toolauth/sla_prvk.pem",
           d="09976537029b4362591c5b13873f223de5525d55df52dde283e52afa67f6c9dbf1408d2fb586a624efc93426f5f3be981f80e861ddd975a1e5e662db84f5164804a3ae717605d7f15866df9ed1497c38fdd6197243163ef22f958d7b822c57317203e9a1e7d18dad01f15054facdbddb9261a1272638da661fe4f9f0714ecf00e6541cc435afb1fd75a27d34b17ad400e9474ba850dafce266799caff32a058ff71e4c2daacaf8ba709e9ca4dc87584a7ffe8aa9a0a160ed069c3970b7dae3987ded71bd0bc824356987bd74363d46682c71913c3edbdb2a911f701f23aee3f8dd98180b5a138fd5ad74743682d2d2d1bb3d92786710248f316dd8391178ea81",
           n="D16403466C530EF9BB53C1E8A96A61A4E332E17DC0F55BB46D207AC305BAE9354EAAC2CB3077B33740D275036B822DB268200DE17DA3DB7266B27686B8970B85737050F084F8D576904E74CD6C53B31F0BB0CD60686BF67C60DA0EC20F563EEA715CEBDBF76D1C5C10E982AB2955D833DE553C9CDAFD7EA2388C02823CFE7DD9AC83FA2A8EB0685ABDAB56A92DF1A7805E8AC0BD10C0F3DCB1770A9E6BBC3418C5F84A48B7CB2316B2C8F64972F391B116A58C9395A9CE9E743569A367086D7771D39FEC8EBBBA3DD2B519785A76A9F589D36D637AF884543FD65BAC75BE823C0C50AA16D58187B97223625C54C66B5A5E4DBAEAB7BE89A4E340A2E241B09B2F",
           e="010001"),
    SlaKey(vendor="Generic",
           da_codes=[],
           name="SetRsaKey in libsla_challenge.so, secure_chip_tools/keys/toolauth/sla_prvk.pem V5",
           d="8E02CDB389BBC52D5383EBB5949C895B0850E633CF7DD3B5F7B5B8911B0DDF2A80387B46FAF67D22BC2748978A0183B5B420BA579B6D847082EA0BD14AB21B6CCCA175C66586FCE93756C2F426C85D7DF07629A47236265D1963B8354CB229AFA2E560B7B3641DDB8A0A839ED8F39BA8C7CDB94104650E8C7790305E2FF6D18206F49B7290B1ADB7B4C523E10EBF53630D438EF49C877402EA3C1BD6DD903892FD662FBDF1DFF5D7B095712E58E728BD7F6A8B5621175F4C08EBD6143CDACD65D9284DFFECAB64F70FD63182E4981551522727A2EE9873D0DB78180C26553AD0EE1CAAA21BCEBC5A8C0B331FE7FD8710F905A7456AF675A04AF1118CE71E36C9",
           n="C43469A95B143CDC63CE318FE32BAD35B9554A136244FA74D13947425A32949EE6DC808CDEBF4121687A570B83C51E657303C925EC280B420C757E5A63AD3EC6980AAD5B6CA6D1BBDC50DB793D2FDDC0D0361C06163CFF9757C07F96559A2186322F7ABF1FFC7765F396673A48A4E8E3296427BC5510D0F97F54E5CA1BD7A93ADE3F6A625056426BDFE77B3B502C68A18F08B470DA23B0A2FAE13B8D4DB3746255371F43306582C74794D1491E97FDE504F0B1ECAC9DDEF282D674B817B7FFA8522672CF6281790910378FEBFA7DC6C2B0AF9DA03A58509D60AA1AD6F9BFDC84537CD0959B8735FE0BB9B471104B458A38DF846366926993097222F90628528F",
           e="010001"),
    SlaKey(vendor="Generic",
           da_codes=[],
           name="bootloader/preloader/platform/mt6781/flash/custom/oemkey.h V6",
           d="607C8892D0DE8CE0CA116914C8BD277B821E784D298D00D3473EDE236399435F8541009525C2786CB3ED3D7530D47C9163692B0D588209E7E0E8D06F4A69725498B979599DC576303B5D8D96F874687A310D32E8C86E965B844BC2ACE51DC5E06859EA087BD536C39DCB8E1262FDEAF6DA20035F14D3592AB2C1B58734C5C62AC86FE44F98C602BABAB60A6C8D09A199D2170E373D9B9A5D9B6DE852E859DEB1BDF33034DCD91EC4EEBFDDBECA88E29724391BB928F40EFD945299DFFC4595BB8D45F426AC15EC8B1C68A19EB51BEB2CC6611072AE5637DF0ABA89ED1E9CB8C9AC1EB05B1F01734DB303C23BE1869C9013561B9F6EA65BD2516DE950F08B2E81",
           n="B243F6694336D527C5B3ED569DDD0386D309C6592841E4C033DCB461EEA7B6F8535FC4939E403060646A970DD81DE367CF003848146F19D259F50A385015AF6309EAA71BFED6B098C7A24D4871B4B82AAD7DC6E2856C301BE7CDB46DC10795C0D30A68DD8432B5EE5DA42BA22124796512FCA21D811D50B34C2F672E25BCC2594D9C012B34D473EE222D1E56B90E7D697CEA97E8DD4CCC6BED5FDAECE1A43F96495335F322CCE32612DAB462B024281841F553FF7FF33E0103A7904037F8FE5D9BE293ACD7485CDB50957DB11CA6DB28AF6393C3E78D9FBCD4567DEBCA2601622F0F2EB19DA9192372F9EA3B28B1079409C0A09E3D51D64A4C4CE026FAD24CD7",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_U91",
           d="8553e31d7a73f6c9294e961815c23f31f2b5ea1116e3c613ae12b26cf285e4c5ca0e2dc8e17d52f96b30cef6ad544e43205933f20ad17eb8712097aaa23116c68eb6328980b8ba26706105656fa65315688b8232758607b8936d0abc27dbc97d94e95b4f1957fd1965082e5849c4185ebba8afc7d558d4f5f001ac5363423ac1",
           n="9a97c44b0768424b6bbb0b6aa987a2d373448c6fee1f61fb81f8cf53d70856f0f77e76c06a6901de90ed3b4d9ad4b9e04eaed42e5657bf2fccf390fe9f5abe1abe8575f07916da69acef95d38874223ec51cb501148a1feea2be2b8ccda08672aa423a4099203c6aa4777fed7353c57696b8e0d4020bd6930b828b9846a454cd",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_OTMINI",
           d="6bc0e84b4f38415bc575dd0d5248c2d182ec55e2ba7a11dfe86815155c709a25bbe34fafa6a9c19344adcfb32eb3d2eca465c2dc0fd7528a00cc268c6657cdff0b0da1b2ac6a95b94865facb7e1494cedf44358e29ec7e8f091172e4ef29856d1f45032aa644efc273f141c10cb8281a12cebe202b65f176e1a145c326d75841",
           n="bc7b5107bcf46c2cd7758f4bd4d4e9f06b731d9cff383dffe48156d1ad91ff74a7925fa3027669766b3d4c6e28c1c9310194c34a59e672c8ced38588e998d7b162889dcf06668345f93e4efca34b5fee5bb57dfc38d7623a48f31b382de2db656ec1f3b5267a9a8f5e441c61448a283e4717ace6983d01b163e34f959c9972cd",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="ST513",
           d="9ea0f7256bcca9099e5db80757a5f3ddeb3292475c01d2e6eaff8da905d9537a5875e874d26872a8c04b552dd310f194ef5a5ea445a50d5c1e6670e5126ef01e5fb1af24a67d07b5a9f72197bc66d5743faab54759fbedcf1fd8ac1aabede2c6fb29601b4734334db92a92fc25f7ed8700d307b74a2c435c9ce5b5caba4b3801",
           n="df836c16bc8e129dac8e6efcd3f41636981687c29c465b481cbe874ffb14d592de024b70f4fa20ad96c96e4e3eded3625f314dedb4d8635782f6d668d04ab1167982229e03ede17a7857a22cbf72444a6bee2bba54f32099e0eabe654c3da4933926db4d97dcaeb68236df4b3e51bd3c4bfa8b2d47c2534405e4f1c1d43e1069",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MPK_U7",
           d="c5829b5bc34253f090db831f5085cd5a6f88da7f6f90e3a3cb6fff6e53218c5a616719971b3f64ef02de526719a7b709978bf1ed48c821981b32ea77c9e536bbda206fad74946d02a20d17120f89419b0daee2d8a47275768930ad53c876afebffb6805483c1ddcf6c19f3566f0de494838afb51b18080beff66364de5294581",
           n="db0b6e89fabdc24e6e7379d25b0c402686537ab6375d8b2407beaf44cbbef27e04e90b556801bbce5eee2a7ec636ac825667dae3578eb7bbb66701bc62ee86f28fc14d57e8637a2ddcee00cc3ab87dff4155250c2dbde9ae62f3d7a9d5e4a265fb0a8b23c082be263d7788e44d59780b47a31b25dc588f81902be419f917933b",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_U8",
           d="76ca90a16bcf7552db2b716b8531fe5617bfe86635627647e3d27291fdf47e67ba8f953ac362dbbce2977f05a9f24aff4250f8f3a14d3ef09b7b99c9384aad0c53104f87b47d7daea3ca725beb233d127ec342ce0619b16bd3d5e44371cffce9f23178ff48dd42fc4450ccdb3e2d63437ef9dfc0296b12840ae85d472cf0135d",
           n="9bc517a0dfa87a7e240000c5f42cf31905ab93d4bcb95694dee85282867d5c83270aea0b0948d66eb39d8500aa6c8b1069b8ee784f75948958f7bbf627d6ed5f286fd3bd4df60a6c9490cb319448b22765aba9329820eec50f62f1ca0b6b3322aa27747b26855a1f1719cf0c4060c9f5a6a3a60ec60fe6e04e7b044e5da994e9",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MPK_U91",
           d="8553e31d7a73f6c9294e961815c23f31f2b5ea1116e3c613ae12b26cf285e4c5ca0e2dc8e17d52f96b30cef6ad544e43205933f20ad17eb8712097aaa23116c68eb6328980b8ba26706105656fa65315688b8232758607b8936d0abc27dbc97d94e95b4f1957fd1965082e5849c4185ebba8afc7d558d4f5f001ac5363423ac1",
           n="9a97c44b0768424b6bbb0b6aa987a2d373448c6fee1f61fb81f8cf53d70856f0f77e76c06a6901de90ed3b4d9ad4b9e04eaed42e5657bf2fccf390fe9f5abe1abe8575f07916da69acef95d38874223ec51cb501148a1feea2be2b8ccda08672aa423a4099203c6aa4777fed7353c57696b8e0d4020bd6930b828b9846a454cd",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[0x6577],
           name="MTK_6577_HUIZHOU",
           d="3d6ff33ae0ec1d029db4a6fb9ca3e41890f5cb5a53bfc0ab3cb2053d85243c7715a07ebfad719bea67c252a223ad0fe65074a5d26ea14ba63ff8d92e553e879b6ce51e065f05b23e5d27deed116ec751c9556ea0cec11e80f3bd206da9e9072fbe1695b19a8a9fcb576f00f7a268df8d6d262127ab3f3246941004f25534ac8d2f418815d15f4a5a663a2f1383115cb3e8bd263ebcd92c5bd1b92644497e15a1b41e77e648cac179182d83c496728fb52b9a1c600954ad0c3eac5d4633d519c88daf775fe090c2f2568c7c91a8938a2859245f100fce764033147d84d79075a81331ecdd170d2541832ab9161dc473cadc1dfbc17df2be89fa6d6c13d9db3611",
           n="ac2a2c19bf4beef4272df8899cb648f90453e53faa1dd8143327978620ec74e6068a8fd051fac856a59ff0a2f3051b7512f55fcd6eea57262a5a24e141b2a9c105509b79976b952a4cfa0367535aa1db83290f18f62e2f604bfd5fee3fb6fa863ca5546e359e0348937e5b62e47f645e9552ebd2e7e516c13a192a6075c55351192dd545dd90c34fa28c695d6643a2449c0c7acc9d003b9bb4f9d249bc19beb8ffdc2d6115260499156461eea896361aac9a24ace3bf6c81db3e8c32fd6d74d876882382618c7ae920ce63b0c33a3ed6a59642acdcdccd68f2e84f6b1dfe8e4dd33fd78208c750f877a8eddbf32b7f6cd28bc7f62a79e1281cad49b29ea1aeeb",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_S_2019",
           d="68d01875ee507057075dd8cf2e3007aebeaf767f350c130684911c483eb918a5e235ab71c2eaec62aa7bbeecdac518cb8962272e83a2943cb0e486b66da8e244fbf3e3d8e4a065198032fdb045f011784127cdfd63d285f7f20dcc37b0ebbdc8b49020b9a16333f196e8e3e8246835b1e76615985ba6e221241d096cc5bdd7336d8b22704dc1576ae0ac252fea8dab129756a609f347d60e25d8d085cf0c8775631d3c0e54e50fc67dff2c55148b4e78cf36987febb23e14ffc1da9cb0adfc139d509826aa98f6fe0e25ec6ab6442e5a7cebbe6454ff06b897467512cdd8f0460201125d0bc9cc2bae259840722ae56d16b06f9e0515a2d128a23b5b0a1896e1",
           n="e4607e6cf78f5e4857bdaea441f8ddd35a7576f552b4ad2c8b4ee7f578c0590d747b049bb5014e06f8350dc6b78d5e0ddff1b4bb8af695e4a338a154596555738cccbe6b58eb43ae221df9babfe9dda6ca770c25ab42ff986f946756b46ec553daf7616f2843dcd6a48f48d9011c050e7ed11c99f61624f057695d622088f868bf6a3966f25bd8ad58db81623fd63f2b91f3ded1a5be0efb69a64bb40d8bbfc251d9c32fbf0a1bad516751e9e04439392c59ba6f856b5c0bebe0dcc67d7d4f25da5342aba94680583ed76d94823c6f62e5e7484f7e2d2a467d167ad3f5647f958dbba3eb66f756c851a55138d1ce465333592969470fa8652df2e38bc380ff4f",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[0x6577],
           name="MTK_6577_SHENZHEN",
           d="6d209285b39ee78c7cfa17a34473855463c8a42d7b494ff0d6885c16d672aed0219193ef388b5aafb3ab10bef394d6fb7831b122ce47564abb084f68f3f7be113bcfc4e8ad3774fbc8eaa8a6fe030e96a56022cd0891f59eb2564ffa2700056e50a8cce72357d3f7ac7ef7b4fdaa69e0ceae1ab3d0f5b90e00414a3cd7bd17afc3b6463ef43bfd22788b68fcfcc2964421b1b622907d8c75e8d83193a579e50c26b0beb93e53e2888cfddafefa03c368c68e6d357087f1bf0800e1bb4f0fc97c092a7e7098cb60cad71e292b506c0cd1f428aff3192da6818351a780aa1b4cce0dccd15adad815b610f445a6571d3c65d2c44da9057b5c8970cded0dfc3072c1",
           n="a29274e3085c260de63f571646cd2c69737ba5a0bf604ad31cf6a86d6a9e08dc931ecdddb7404f4c9255c72b5debdb69114146bdd7edf6b38505b19c4d18eb0e71516d4faa871cbe1d2e24e15c1877b33587a8bdd1e7dfe1b17235d1ac431c27cae07804014c287fbf2479e6b4b80665898f7cbaa7edcf23daa8dd95f63039fe7eb641ad7c05e221d29adc62cf84893ffc6acfd44a9d2cd60d5e0f94d1c29d317bbddb3f5a324648069c72857cfc708fc9bd8a3f7a98051fa9835af1f9c71d80236334ea51cbd52e57e5a7950beb394d9c97bcc32591d9700106b0abfe1dd2db9617fb7dd2eaa3885630c3ce1dfcf087c814b480f30c411f3071f12aedee4077",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_S_2022",
           d="3be4c4d89124e53d12cdc922c0c6571224e8925fba160186068855c5032de6655be49233899432008faef8ba5037f1a0b237e169f6f9f05be2694bf53d04b44507fceb1480007d2f49c8191ced7528e6b4fb06070851c85f2025ccb60271631def9f831822b351ed17ca9a165aae97516a6c3940971d17e927f3befb43432c1b689cc660a896237f090d7b311d9e39aa1eee5a4e3af00843c965c30ca9aa5dd7767809d27d4f66777661779d2a1fb90b014329a1973e67b8989de924e8ac98673667e4f734382f87f0dd0300d360142afa772d5beca2ef248e90a7bd32240c4a5b5f41aed3f4b63f90642f138186fe17afd713a3242eea7b2dd0f32b06b67681",
           n="af823063550d6e5adcca01a1ae1fe357f73d7e5c60cfa25e4beac24304b70623654fd13547de869899be532f45f3c5ff26b50292dccd112dda1478721c05304445058499bd00f6b104e16fcf2d0af55781be147787227eff54a25dca42b9d6f1fc8f4b821c099f483c402addd178330167aa9b1021dae121bb2bdcb0127ac47ae866a1579f2399c70e69293ddd3b0bacec2df9dc518aa0c58c2d7561c5783ac32e57b91d16d6c57764755894963733b85f19f9a3bcbf624199cdd1b31cbecc5448b132c3799e2d0e569f0ba61245796db5876820ef125f4a230039c5cd16b2414855bf3a3b565f81787a4e9b264c9bc855b4fe7ac17caca1bc5f070594a9c175",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_B3G",
           d="12ff6a160cda225ddc898cc6ef7dd3c69d05dc24d23b7a0334568dc85191f3b63d278ab1c8449507dea8533496e04c77225a12a27b7abcf34d10c3cd67b1b41d7c19c44114e344a74396541d998d7b76ca06d0322bf3333684652528df22021c190bc38acdac2a3be6e2d0bce7f1e3c77a71750ff17895cff9c6225275a3ce81",
           n="cf8243d13128ed39fadad9ca97c15585d634f4d9b38dd59e4eec4b0b93e4eb2fd2d96c425855e69706d5c11021a8c2e08bff87b424bed2dc3efa9360bf1bcf80c96cd4ba9c39eb79bfa2bf9d4efc5a56798ccd9c6599ede595aea644086605fbe55b2f7719fccbafe0c95956fcffb0ce77a9637c9ed66e067165cbe901eb041b",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_E8",
           d="95b32d61a10e6c2a54fa4e5e020d590f6bf0f295fa87fa03b3d00dcdc4982dc997ad5c7ff872255141ec1b77f714c14587ffb87c985531c937b245062ee03514aa796ad79698c40c49a8b3c54ec66fc20deb874a8bbce87239c414f541367a350d525fa6bdea77e4cd3078cf7ddf22a8aefb0c595a6c76285d837008c0a77e29",
           n="bdef438901dfa726cfc2cca59d12f009108b8e1fd7dd9b91a5cc71fa7b1e36c8783f9de5850050e6505fc715c50bddd59a3064b05214c4365360cb98d080cc38658a94695184b564e8e8dcc28f70eb0122a4bb7662e3a1f34c057ea523819ed02ed46bae0cd9530b0536cbe7a1ba3f33a45feb2f92ff5104dc32ebe94f249eed",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_C3G",
           d="4375be875664fad432cb6476f1c7aeecaea3166a51eadeaa32e96d0d79dd159b6287f4cd42685330fc15391eb4ee83dc6fd22a913c5fd5023d8fd6b71af8b530209b5355acf1cc6e6397aa6e5d2dc92b7d37635d391cd22a3aa337d8fc0a274cdd7d6630395d13517e32c91daab2f5378ed7a1be86c81c2e775c249201f2c221",
           n="c04e6a1be49c5a57accaebc837099b40890180fc046c3dca58745749d0979cadb63b8b4573fafc129c2f89ebb64c4ec81339e862f5638ae145e2c8bc291097e6b90434ff3f3a1e620fa77dcb6d963f53b79abaf4eefb8a5d4378cdf4ab3060a9901909fd455cf850ae5adbdf035cb3cbcf572ac4dce4bc1321562273a461ddf1",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_K6",
           d="4f65cda0c3ac66753c58d748db46bfb8cb8dbd1f849c7444afcf37dc6bb218904c5a2fe08808680d2a6e7587681256a6ed9751046fa42ce44874bf2061f40dca4953c345c2f156e8ee7e2f497ebc59b3ddccda98584dfc999d213d6782f2b0faff59a9671cee801defeb5a51178a7b95c487aa735b463e8b1321b6ebe58c7401",
           n="a7e3089840bb7a9a7a972e8c88d7c464fe40dc4771a2df0da981079cc800f5d3cd45ed9eb34efac6bf7d2aa6dbc1266285f50d7e86e6e0e5dc6d062bc8fe871672139904e5ffe64c6ffb4ff00817ffc0ad4c18787a253ba5f7f7bd8412e5f46e2c264cedf174ed5163943331a658b434c59ec9e11b269e829ab638c80c4ebe51",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="OPK_VLE5",
           d="4befe0eb0c424d83cd2dacb59740cddec599ab3c8833dee354717425993d12ba5441056297153bb3d2667c3e9c76caabc349a07cfab60efa9e5e7b35e971fe7eedac090a1a5a7d8a2cd59de84762f09cacffecb65bf70ed504243721fd0e094c3f216fbb85778ad82829658232a2f472919e992060394e79f2aada9e8a42ce21",
           n="cb676a5de86e2c7d75a17f10fb2e3f81a473e5d2d088833d8c1928ce78caf1000aaa607c83f55b57dc07fac7a9ecad1600df5d033986c02c003884620661a9674042a835b99cf8a024c27a10410eb379ac69e72d6f5a9cf72c185262331c98879cbc225de835d864983d2bd085f1df99341d3cbb0ba3b0a50491c8ee98d691b5",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="OPK_U7_1",
           d="18e2fa361f4e7fc86574d9a93f2113a4d99d272710f303e29e07ebf71444335ce789dbf9816d472b27935ad49202379e44023071706bd0058e2bae45ace0938e75610579240ec87086d27fc0844ba25bba09214ae43037cb902801a58915ce58c6f805fb3ad6cf7996f25e0cf0a94c13e04eb4370ed6b93c39ba2136f8cfd101",
           n="de15dc10818e30c363bd0a87d5f8d89b832329fa25b8388709d94e9b0ee4efdd3e24eed3d931f01ea1b0e2b76265d7dc270ea8012545bb7245c286761210bf46c6dd1fadefc257fabebba29bbbd86e8336460e5d21888a319156e8ba529e4b6a200136ae4aba447fb37a357028142d8b16d79a421d513ecd9b9ec0d908ba8217",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MPK_U7_1",
           d="88a4477997b57337cb144d0656bd2d5f0ef59d6b574b631a79ac8015a4c20d454e1df85682ad25eccc7fb92be373259fffe58741b5a85e50caa68b9fe84f6e295d2176b96c20ff819e8bb889702c474effe1a77710ff3b93e896fa488f1717c75e46a1b0f5898fcacfa35943f1abf80ebb665ba7fde59c4baa61dd2f6c5ec001",
           n="b6a33b825b0cf6abd3c9d39d1c8bdce50a41f9bd5ca2de52c4c447afa9943f5c1365d2e9cb7961ffd877fd38696b4479a8bb7eb8da15bd8d59a1cd7e5ee517d1a20f29bc66974f87796a11f7537529f8f46ac57861484808bfce9ee6cd6527f7fe3bfd57b4a7fd46f8dc047d6c8370de6507620c2b9a3bf864e8ee4c4d2abda1",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_S_AT_META",
           d="8294e45929b8f95a380c59fe715da5225fd518920a85fdc9a8b2ade6675b7680293c21539fa4466907cb3601b072d8adebb0481ecf069baaee00d0f5cb4396f4ffea11dfd41f3c62fdeb312ee9b4be2026bc40aacd9ff928130fa7af0305228dd5e47c551c2a701653dd6841b9566099de99e2731194ae617ca8d9df99a47c49d9f514620ea1e3742da8dc7dec6756403631a274dc226c6121863e4a571a120b63c38d134853df5b986fac1565e1f3bd8a02d239462967e9c71cedd9ae0c0eec330018ca553cc7cc2fbc73d6ba37be2fe360644ff69ab7c734264675c057417857df4ca206dfdac9a5621f9d8e45dd2e58dc8b4198667de3efd1d5bd7ce007a1",
           n="d1eee63f19d148c904076c507aa8d4f6c7e931a65476fe5231c06036fea2ecbcb8c811882c4f70e6e3523be73f5c7a83570f3a40bd894399a5ee9f903e8e745ec4e4e034495175b167192535843f06241d6477e3ce1ad5270e590db9cb905404c01aa407433fa2c2ca1f8366c1623fa45bd5ee68e3145a57f9af3e6e68fce41b8c682c0e07f3c48f4b377951b23b467fea0d4ee0e67c0235d0e83ae27e40ad1c060063ceb966835a0ac1eb68066f8b55775ceb7b444ffaeec19548a42247ebe687f881a0c8e5277beec22241e2ddae1c21cec8046eb005302812b7ef42ac153cab317bbeaad73f7ccaced38c433530b7e0ad464150026025a9a3ff5d45e025db",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_B7",
           d="776b1deb8c3e943b3dae67cf2b597ba55c439dc1fa10e4e9ea530df96bd0815cc3ec3ef0267f89a699c5cb64bdb91e5e9ae4c7af03cbcfbfb4755cda55e3a31d510f96a102b5aed90731788a426e371f8ae24f660403377cc0836a06b2a8e159bd177f4cf68e36d447e4b52ca63611cd8416c1efcac52143106c272f7474387d",
           n="e3e3166f47177de4915e915a9d555d980afad96be22cbb8a02516ac8fe69657bd10bc6d072046dcd33e4476e24f128cb7ac613df140cefe71abf080a74d27c114635d3954c55299f6f81c2a0aa14c4c678307f4b3bbf0c64f0006051ea7573b5b0cc290201c76c4d272c981b1bb19bd0a0a0ac046e6e63b0f4cf88d2c98a5c91",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_BACHATA",
           d="09fe029a23ff7e37c749386fcc9a640450546b95e5127489d364d380393c99f5c10da6d7cf0ed955f4a5f3d8d90d97cc7c49069d394206f9b59c11568ffe66163eae377447abb103cd5d4256885cf7984b28cff8a096dc479b9196d66cd534cbdfece7a61de04110bb14a3ba5e0f20ae0bb4d82e18fbff0335904dc09b829e91",
           n="94cc529bb1af0ab8043f09e3ca612d787cc19485d3769546e750f6edb844979ba8f1f9afb8b93b521330b74713831a78a584f7b24780f92dd00e5d56ce8defa3cd39d01752e514a4c2ba7499f334729622049491b1aecee6c9e1c867e996c294b10f5d62ea4504e333424b280162087296c300c01fdf75f47d874df40dbdb94f",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MPK_VLE5",
           d="7005d1bf5be81db7b17c9b16b1d407b308b42e3490e75a93e9d00fd6c812d1d8db2f1041a342964808a037f315a448ecaf0502a5215c58f0de709c5bd87e3a65e0291a1a23547c76cf437ef1d9b434b70dbb417049a31de9ee7becf218a5bb63b05fb84ff49d1e6aaa4b9b4376f47417435ecd85ccda63be9070e7892ecd4a41",
           n="a62bf756a70657b6b560588e85e662e181b6a61ae466ac3d0d2e971f160e88216792cedfb1979b3d6b665068eee8a8699888cd74ec9482c61ae7eae3571e50beccdcb336477c26040d09b46dbd93efc0fece4adde2e00c1cbedafd6ad7c43bd621675a6a46425c5cf6182fc5602be443a372fb4ead4531e64285ce29be913285",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_C7",
           d="31d28ed040a8ace0d56fc94b4a7d29dbb135d62c7905621818d657499fd6ff6fe7417592cececdd3f3d37ec0a361228da34d3e7a2724b7832ced00008fb4ae500357fc3d285c64fbf7efd4bd1ee48ed40190296171acc3c2d0c69e89da5a8fde7e0ba7048aec6bef1bb19646f883fe9d77d8d263545e7c00e8604be38210d065",
           n="c1d6c392828f4620e455c138840ab448cfcd4aca821663335dba9c51dec9b8198301ca6b069adefcd1887f1cec31c15674ab264daeeb82398b419f08b4236904203c48a7db8724f1773d04a6b8c88cb38907a00bc53e86cdb2bbf479a68b8241382bdc5ac6105270efc2da4cb91a36459ccf6a2a87dd56ec4c331dd419ba5931",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_MARTELL",
           d="985e549fd42c0b4955d3db8c3ee601f65e10a3db08f957fab4016dbad0f60c7e09e8b7a782404cb0fc7c805dfd67fed814765ed58b7a146ed2c1d31b80e3f845a45b6ccda5a0344247be404c23debf027c7b5082373372b49bf78d9058caa66c57d3be829088c3610034faf1ea9f24a21110bbb3865182747ca1779e83c6983c189b3f19f3df49e5f9cdfa57f4f69dfae53e19ee0b1ec30986d59ad11f52bdc022a9499dfa89f8546d266f6026aa307501ca5a619f5413a45ef38f139c3ea8b52f02fbc8983aa878052d9108668ecfc8605057a298355d2f680c34630e224c57dd4c4f2dc0d51766ef7070daddfa3c885a3f94d76c943c6c1054d338e2323b99",
           n="a800d061e4a42e4c3453a17cc8daa974e23bfaa403b4a60fad6d3516d8ec035c1ebabdcd60009d9b8c639954e616c6cb6cf821e31e58772ffc366e6ffb7314657567b12279a34dd69e46b8a4a628dc2dfabc68fa1d89388d2058a97d2e31520b4fb04bc2f963e110e8541eefd22d90a03eca806b3c6a20c6bd1a7468e61ea1ab283ed1bc462dfae189eb5fb451f802fb868cda9a7409aa52e42b18882e79f4f1c2377829fafd9760468bd1db823bd9080378cf46ef405d91636cafc03acad9fada6b0446dbaf51e9d533887e4a3a8f62114063e0b8920684c28bfbe256aab26e98751166358c201347ba6c3b36d49aab6302fc248eea3c254e15a08429fd2149",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="OPK_U7",
           d="61ed86791440c26491b763730f483c18c32fcd77bdb6f9e9e3e11cdfb9716d22c392c68556219e2b6c1ada57649ce2de559c239a9ff8f33252480421e4a2649df8e3ee0095c9bec361f25a5ec67d0b4d96c73404ff8a115fecf1173a6568845480fd4423b5dba2e5111335655f3bc2f3fec65510648571992e010ba0aaf243e1",
           n="9f94e8f1171fed4b427629c928e807b2220f109ac70a3d5b1b8cbd295bc3fa3226d3903298cd81319b9b08a6f8e77efad0b04139b686ee0d1586175913ad6f65d6cf21bbc7f769885381ba6d840414b26fe7b9b3e393acacb3453e3a0cb79ca21cb38a42685a03462244fdb2a5f1d8b9e20745fb3206e799655c47146310911b",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_S_2020",
           d="b86887499d157d3b1feb1041b9d2e94065732b41d22feebce317676321d66d1babcc7a53544e35a714c207811e62d134291d616417295e5b0c4aa3d65e40b41a352822263c22cbb4041a1883c76b97a8c925cb428a7b2300622ddaec62209d8dc0c60159f6c7ccfc26768bc469deec22bcd62f49f4c2ca1b2cf0be49d6e5ec563279cdee79c92800c6c965200d316c79285551a54359b37ec4173eadf4c0506d857ddca4831ade7ea8f13097b4e2b630a2d3eb9c57abcc65f84d693c55e361763d8d37bb40cd6e2520684ae05edc62a36cda6747509600f4605b7ed924ee1ad49e66eca1176a20794600173dbb42fced2f1fa0cccc0af3b56d58453bee420099",
           n="e4cc4967bec817bb348468024c3084b15fd4f7810c8a9d078a4f51cf9974d2e3bae8d5a19a85c0a73befd0675100e642a3f425e3192dfb1de56928c37f45fc142adaa65798ada863b84d4b5f22c3f79b95cc201ac7c292c99475453a62b7b7e06e84833dfca7a0df931084932a80129e543c6d24a13c5f2cba6ef5ffed9efd4dbc20496f5194f0d1aad9d789f32577f8846df9a14778504ccb5dd7507114c148c1937fb99da15f9596d4fa052cdaf1f66d7e5e0c0793628752bf9af3c4ac67e21c21d170ad448160761bddf586a4900fbb7dcc44467f1550d15db774d7cacfe3105b465321a5f95fec22c2011d616a5c0e22f0535dd1f969202be56ec015f891",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_U82",
           d="3f5d99a61561d70c6c335a30d9a11fa8a3ad70fbecf46c9e233d57aa827cccbb137c060a47e693e234ba1b532851053e17446d5582b9fee205c0d12c7613378c8b8c8c0184cdba90d56a308014aac0458c5572699d599a15ba36146b6f2e230034708cf67d31ab837b7bd8e5967fd9a7bf413b7d9314302b18e48962d01cf6f1",
           n="ed2055a7b95db86f7e3101196ae6218015d70d03df6fd5787de150e82927443097a90485757743447e2f4641afcf510acf585f73e79c45b2908d5de8835221a76d93e48ca465ffbe0dd76cdaa98550ab2e7b84a6470d48595742fb54a204442ce67bab989c69adf86457e313eb24c87d80aa7d635449fab0d97b6b08c5f7c86f",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_JADE",
           d="69fd6b9e25ba604e204ec90e8e0769b28417e6b52dda7ac53deb712c549f398a48ea8ad20bf065a093ac85f336f92f1221d3413f3793bc8c7c6057a091828c04f6fb695f43747d0d22de100bccce70ac7a8f9d092afaa7d44fcda99b12454f8c887e383c69e7e21ad15203eaae51d803cf35da09c8d536139c658bebfddccf01",
           n="e8490dcbd3488278442f78ec5634ccdb8befee081ed0d19071480a10c299416ab8d0e9eb19e8975cac260606463c51bb62875ab24690d07905b9c48fe60086da12899bce3dbed91e0157cff76f27a1c09b37e837e7acb71da3c0e30564223ae20216fbcb3de5e93c2d7f98827d61441b988e57497c1ddacb87cec1e73139bf67",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_B82",
           d="88a4477997b57337cb144d0656bd2d5f0ef59d6b574b631a79ac8015a4c20d454e1df85682ad25eccc7fb92be373259fffe58741b5a85e50caa68b9fe84f6e295d2176b96c20ff819e8bb889702c474effe1a77710ff3b93e896fa488f1717c75e46a1b0f5898fcacfa35943f1abf80ebb665ba7fde59c4baa61dd2f6c5ec001",
           n="b6a33b825b0cf6abd3c9d39d1c8bdce50a41f9bd5ca2de52c4c447afa9943f5c1365d2e9cb7961ffd877fd38696b4479a8bb7eb8da15bd8d59a1cd7e5ee517d1a20f29bc66974f87796a11f7537529f8f46ac57861484808bfce9ee6cd6527f7fe3bfd57b4a7fd46f8dc047d6c8370de6507620c2b9a3bf864e8ee4c4d2abda1",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_S_2021",
           d="cf553c03ac3cf21fdb4097d4a97f35fc6c305a2e30dfbebb7667ba2adfdec99d3277bccd314281c592ade680b42849fde6122659a68cd7e525b764520d612c7c6c141bc4b2594bc88732d4ca0a97e464d7c1ecf4fc2788f1920cb030c1b2b3ea84e8d6191d5e53d56c5fc495051a1d0fdbea947d58a9d773a68152d157d4bf57f2b4fba8182f96ea4c9b798018361054f95b251089c786be542c7881c49b077ad52af25a359bb26257170706217f66533cf4b8379a1fb7a30c955c8ed4c1c6dca905ce6e7e5e92ec7e1bda1db44cd187a9e5137fe44a37cfdbee173a49654994926cb2fdd7857dfc8978d9de73e899e18f5dfe33a64e6414fc5d93738f8c5591",
           n="df85f4c4ae8c98e78142d403d002276a5bf9edd17870caa848fc45720e8b4be94f6f9a47181417840a5b7d4fc36575129afd6a848a0de3f62fac5b5f687a2219cab8cdf2e7527d6af3c6be84eb99bf519b0b210960fc8f5223c9bc38e8f20d0267642153cf370312b955143e10490c6a207868ac7ac314bbe10f6063a1ba606e28d248a1ee3e7000d12e9c4ebd47ae483b625156b82026fcfdc36118198cac1463aeb56bdfe260efa38ac1d4123c13fe59e0fb0f2f895609c117f7a39fb9f27c356d4748cf7af41e15ea68c6c7c64c4d0a1acb4632965e0260d9b08de9fd81b82050c9929b79ee865f89272483b6fed8a409d6a1af2429d24fd358a4b4da4e77",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_MINIQ2",
           d="a475ba952a9f2f9e58d6ec91b41a03158354ea1e451656d83d15691c07eca3410e7a2401283462f66a0ebf1f91682a80ae61168b2260f4368f93e197a9db65f4139523ef5449a6fa77568a9ffe90e0a34a37f99b7c1ec6ed1683a574d9045993679ef73299991cd43b96fdba6673ae4318f2f635a816f8559d325f9ebe428a01",
           n="ba1d10a245e60471e8d3138611615170f213cae5b895c8af35eb720e2671915f07dd6ccb5384d7580200d18f430c89405dcb0be6a5e91cff0fda970e292d5f0704720473bc61e19590539b1bb08ce2b306755db1f70cf1193933802ca44281fe01699f75e56fb7660fce0342ccc284d497a17ad7d3d15eaa20ad4c67bd92de61",
           e="010001"),
    SlaKey(vendor="Alcatel",
           da_codes=[],
           name="MTK_HIGHWAY",
           d="5407571c851f5b877a2255c6887c5d832369698b481c81db8ac07062dfabc7229d4b00f95956665743f7deeedbf54a17c9a404c97433f46d983bd0c5f49fa4b013b9d86e5f1377f563d8299675c0ea2b81f51c33ad74a265184df9389eefb8e72d2f0585e4a41826b8846b0ee6da5ef8cce471536109fe4c658735247ebbc301",
           n="beca753fd31ef104bbb01b0a7c560c7bc040d30ea18f216b64b7de416b695af2b3350ecc02fa5224b412793f876a7bdbd8cbe7fecd754aa8214a27bfe7ececd8caa16959df83bdaeed524880a820f8dfe601dc70f164ff1921baaa06efd8c584c22269a109d16287356fd30e7eb02a1365ca93fcb8088278f119a2c7298306a9",
           e="010001"),
    SlaKey(vendor="Motorola",
           da_codes=[],
           name="G13",
           d="AEAC47CD11A5DD6C5EEEC43D8F2C536A2917CEF95AD02F5A7C978E88C35702B590F7A72A2AF28AEB9B5F5B2D8056D03F916595D189C9B6927AC0874980537178AACE8E1831DD654E0B72FF2F44670196A57A43C340355CAF828B331A5715AED4E06D5D18896BCF25B201A0DC9760B0B2EF1CFB4EAB6940D7F8E2EBD86DC1E678AA69F6B0BBF55C688BF72C2123CF42E367F789E2592CE281C7C4752E14F6FD00D54610977DEF753E3890F12F704688537E860D81142805750B805E7CAE3AACDE1CD7A272D227E9F8CCAADCB4D06489664627BAC46CAF5DA0F0740CEEDEBC7ED1C1D1EB1E37C6A8A9E6A0454F742B3248448B20C93D5FF6E5C789907A862C90A1",
           n="DA61964924F441559A1F8B5264CEB01DACE8E417413BBA4657F4556811D07B85074FD6987F315A7492E003D03C57FC83D3B889F2D4F136D0989E515A08628A7B16A300217162DC35C340B1127046AA86649B763AF97F7C9871964483DE6695CDA2E8CCE82E1F6A0F701AF8BE767BB16927489524F8FC9A2C280F5692E850E4C4E2606436CF2E253147AFAB32E6B92A19FA180C43CF480619B71B3D6A7863C7CC376C0A36BCF8BA3DA89CBF3E6DAA4691DCD769C0AE4535E502A9966AFF3F123C7A0EDA2DF04593B0E1FC60DC688F2BA7617DFE67D31854443ED95D2645323728C594CA49DAA9351A572E3182D0A1B3146C92CEF87380CBD2DEFFEBC4E8F420D3",
           e="010001"),
]
