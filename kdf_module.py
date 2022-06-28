##
# @file kdf_module.py
#
# @brief The base module for the Key Derivation Function.
#
#
# @section libraries_kdf_mod Libraries/Modules
# - MP_module.py for Miyaguchi-Preneel 
# @section references_kdf_mod References
# - SHE Specification (https://www.autosar.org/fileadmin/user_upload/standards/foundation/19-11/AUTOSAR_TR_SecureHardwareExtensions.pdf)
# @section author_kdf_mod Author(s)
# - Created by Satyam Sachan on 06/23/2022.
# - Modified by Satyam Sachan on 06/23/2022.
from MP_module import Miyaguchi_Preneel

def KDF(K:bytes, C:bytes):
	'''! Implements the key derivation function (KDF), as in the SHE spec. 
		@param[in] K The key from which the other keys are derived. Needs to be in bytes. 
		@param[in] C Constant. Set as in the SHE spec.
 		@param[out] out Derived key. Output is a hex string.
	'''
	i = bytearray(K) + bytearray(C)
	return Miyaguchi_Preneel(i, 0)