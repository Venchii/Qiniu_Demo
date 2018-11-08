 // OCR身份证识别接口
    public static void main(String[] args) {

       // 构造一个带指定Zone对象的配置类
        Configuration cfg = new Configuration(Zone.zone0());
        String accessKey = "RrnoWYRZS5qrZBYqkQ2RNAcCTwtcqCiBRFXFlWej";
        String secretKey = "eFZjKLqv2z1JEDwFqUjUi7BhFma0Y4S9836asMqz";
        //默认不指定key的情况下，以文件内容的hash值作为文件名
        String url = "http://ai.qiniuapi.com/v1/ocr/idcard";
        // 构造post请求body
        Gson gson = new Gson();
        Map<String, String> m = new HashMap();
        // 这里放在空间内身份证的链接
        m.put("uri", "http://pd4ivutut.bkt.clouddn.com/0f7f45b8-c1c2-4742-a20c-469a38cd4408.jpg");
        Map<String, Object> m1 = new HashMap();
        m1.put("data", m);
        String paraR = gson.toJson(m1);
        byte[] bodyByte = paraR.getBytes();
        Auth auth = Auth.create(accessKey, secretKey);
        // 生成token
        String token = "Qiniu " + auth.signRequestV2(url, "POST", bodyByte, "application/json");
        BucketManager bucketManager = new BucketManager(auth, cfg);

        Client client = new Client();
        // 请求头构建
        StringMap headers = new StringMap();
        headers.put("Authorization", token);
        headers.put("Host", "ai.qiniuapi.com");
        headers.put("Content-Type", "application/json");
        try {
            com.qiniu.http.Response resp = client.post(url, bodyByte, headers, Client.JsonMime);
            System.out.println(resp);
            System.out.println(resp.bodyString());
//            return resp.bodyString();
        } catch (Exception e) {
            System.out.println(e);
        }

    }