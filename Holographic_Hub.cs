using UnityEngine;

// Renamed class to match the filename for consistency.
public class Holographic_Hub : MonoBehaviour
{
    [Tooltip("Rotation speed in degrees per second around the Y axis.")]
    [SerializeField] private float rotationSpeed = 50f; // Expose speed to the Inspector

    void Update()
    {
        // Rotate around the world's Y axis (Vector3.up) using the configurable speed.
        transform.Rotate(Vector3.up, rotationSpeed * Time.deltaTime, Space.World);
    }
}
