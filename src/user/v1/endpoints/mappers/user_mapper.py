from datetime import datetime
from user.database.models import User as DBUser
from user.database.models.UserDocument import UserDocument
from user.schemas.Address import Address
from user.schemas.UserResponse import UserResponse as ApiUser
from user.v1.endpoints.create_user.schemas.CreateUserRequest import CreateUserRequest
from user.v1.endpoints.mappers.gender_mapper import GenderEnumMapper
from user.v1.endpoints.mappers.user_status_mapper import UserStatusEnumMapper


class UserMapper:
    @classmethod
    def to_api(cls, domain_user: DBUser) -> ApiUser:
        """
        Maps domain model to API model

        Args:
            domain_user (DBUser): Domain user object

        Returns:
            User: API user object
        """
        return ApiUser(
            address=domain_user.document and cls._to_api_address(domain=domain_user.document),
            createdBy=domain_user.created_by,
            createdOn=domain_user.created_on,
            dateOfBirth=domain_user.date_of_birth,
            email=domain_user.email,
            firstName=domain_user.first_name,
            gender=GenderEnumMapper.from_domain(domain_user.gender),
            id=domain_user.id,
            lastName=domain_user.last_name,
            modifiedBy=domain_user.modified_by,
            modifiedOn=domain_user.modified_on,
            status=UserStatusEnumMapper.from_domain(domain_user.status))

    @classmethod
    def to_domain(cls, create_user: CreateUserRequest) -> DBUser:
        """
        Maps from API model to domain model

        Args:
            create_user (CreateUserRequest): API create user object

        Returns:
            DBUser: Domain user object
        """
        return DBUser(
            created_on=datetime.now(),
            document=create_user.address and cls._to_domain_document(api_request=create_user.address),
            date_of_birth=create_user.dateOfBirth,
            gender=GenderEnumMapper.to_domain(create_user.gender),
            email=create_user.email,
            first_name=create_user.firstName,
            last_name=create_user.lastName,
            status=UserStatusEnumMapper.to_domain(create_user.status))

    @classmethod
    def _to_api_address(cls, *, domain: UserDocument) -> Address:
        """
        Maps UserDocument to ApiAddress

        Args:
            domain (UserDocument): Domain user document object

        Returns:
            Address: API Address object
        """
        return Address(
            addressLine1=domain.address_line_1,
            addressLine2=domain.address_line_2,
            city=domain.city,
            country=domain.country)

    @classmethod
    def _to_domain_document(cls, *, api_request: Address) -> UserDocument:
        """
        Maps Address from API to domain model

        Args:
            api_request (Address): API Address object

        Returns:
            UserDocument: Domain user document object
        """

        return UserDocument(
            address_line_1=api_request.addressLine1,
            address_line_2=api_request.addressLine2,
            city=api_request.city,
            country=api_request.country)
