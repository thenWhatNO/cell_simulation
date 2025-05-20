"""
| Marker | Meaning                          |
| ------ | -------------------------------- |
| `rdis` | Active radius in pixels          |
| `chaz` | Chance of being activated        |
| `time` | How many generations it's active |

| Marker  | Meaning                                                           | Use Case                                                          |
| ------- | ----------------------------------------------------------------- | ----------------------------------------------------------------- |
| `cool`  | Cooldown — wait N generations before reactivation                 | Prevents constant reactivation; like refractory period in neurons |
| `prio`  | Priority — higher number = processed first                        | Helps organize conflicting signals                                |
| `inhib` | Inhibits another morphogen by name                                | For mutual exclusion / regulation (e.g., `inhib=move_right`)      |
| `once`  | One-time-use — disappears after first activation                  | Like a decaying signal                                            |
| `temp`  | Only active if environment temperature matches                    | For adaptive behaviors                                            |
| `link`  | Link to another cell or gen product                               | Simulates pathways or interaction chains                          |
| `dir`   | Direction — targets specific compass direction (e.g., `dir=left`) | Controlled spatial behavior                                       |
| `mass`  | Adds simulated 'mass' or cost to expression                       | For growth limitations                                            |
| `age`   | Activates only after N expression cycles                          | Delayed expression (like puberty genes!)                          |
| `tag`   | Arbitrary user tag for debugging or filters                       | Meta info (e.g. `tag=debug_color`)                                |
| `vol`   | Volume or intensity of the signal                                 | Could control effect strength or visibility                       |
| `type`  | Type of morphogen (chemical, physical, etc)                       | For diverse simulation behaviors                                  |
| `decay` | Rate of fading over time                                          | Smooth fading of effect                                           |
"""