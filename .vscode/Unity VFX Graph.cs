using UnityEngine;
using UnityEngine.VFX;

public class HologramEffect : MonoBehaviour
{
    public VisualEffect vfxGraph;

    void Update()
    {
        float wave = Mathf.Sin(Time.time) * 0.5f + 0.5f;
        vfxGraph.SetFloat("DistortionIntensity", wave);
    }
}