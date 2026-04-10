# Tests of Technique metaclass

The test matrix for PASS conditions is as follows:

* `uco-action:Technique` is:

   - Not specialized (see `ex0:Technique-A`)
   - Specialized (see `ex1:Technique`, `ex2:StandardOperatingProcedure`)

* Each of the above degrees of `Technique` specialization is instantiated with some `Action` subclass.

   - No specialization (see `ex0:Technique-A`)
   - One level of specialization (see `ex1:Technique-T0001`, `ex2:SOP-0001`)
   - Two levels of specialization, using the same Technique-subclass (see `ex1:T0002`)
   - Two levels of specialization, using different Technique-subclasses (see `ex2:SOP-0099`)

* Each of the above instantiations by some degree of `Technique` specialization is instantiated.

   - No specialization (see `kb:Action-a34208f4-31ea-4d78-95c9-153a73fbb628`)
   - One level of specialization (see `kb:Action-c44d57af-a6c3-4350-b08b-0dac5f3b7aca`)
   - Two levels of specialization, using the same Technique-subclass (see `kb:Action-8f84a98c-2ab5-454d-9c2f-443fe64b7158`)
   - Two levels of specialization, using different Technique-subclasses (see `kb:Action-f6625d7d-978d-4562-83d7-23d9ac398073`)
