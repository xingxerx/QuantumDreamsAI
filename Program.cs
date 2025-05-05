using UnityEngine;

// Ensure this GameObject always has an AudioSource component
[RequireComponent(typeof(AudioSource))]
public class AmbientTrigger : MonoBehaviour
{
    [Tooltip("The sound clip to play when the player enters the trigger.")]
    public AudioClip bloomSound;
    private AudioSource audioSource;

    void Start()
    {
        // GetComponent is guaranteed to find an AudioSource because of [RequireComponent]
        audioSource = GetComponent<AudioSource>();
    }

    void OnTriggerEnter(Collider other)
    {
        // Check if the colliding object has the "Player" tag
        if (other.CompareTag("Player"))
        {
            // Also check if the bloomSound clip has been assigned in the Inspector
            if (bloomSound != null)
            {
                audioSource.PlayOneShot(bloomSound);
            } else {
                Debug.LogWarning("Bloom sound not assigned in the Inspector.", this);
            }
        }
    }
}
