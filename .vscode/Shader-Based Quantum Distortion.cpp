Shader "QuantumDreamsAI/HologramShader" {
    Properties {
        _MainTex ("Texture", 2D) = "white" {}
    }
    SubShader {
        Tags { "RenderType"="Transparent" }
        Pass {
            CGPROGRAM
            #pragma vertex vert
            #pragma fragment frag
            sampler2D _MainTex;
            float _DistortAmount;

            float4 frag(v2f i) : SV_Target {
                float2 uv = i.uv;
                uv.x += sin(_Time.y * 3) * _DistortAmount;
                return tex2D(_MainTex, uv);
            }
            ENDCG
        }
    }
}